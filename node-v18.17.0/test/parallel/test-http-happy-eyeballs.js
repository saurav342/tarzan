'use strict';

const common = require('../common');
const { parseDNSPacket, writeDNSPacket } = require('../common/dns');

const assert = require('assert');
const dgram = require('dgram');
const { Resolver } = require('dns');
const { request, createServer } = require('http');

// Test that happy eyeballs algorithm is properly implemented when using HTTP.

let autoSelectFamilyAttemptTimeout = common.platformTimeout(250);
if (common.isWindows) {
  // Some of the windows machines in the CI need more time to establish connection
  autoSelectFamilyAttemptTimeout = common.platformTimeout(1500);
}

function _lookup(resolver, hostname, options, cb) {
  resolver.resolve(hostname, 'ANY', (err, replies) => {
    assert.notStrictEqual(options.family, 4);

    if (err) {
      return cb(err);
    }

    const hosts = replies
      .map((r) => ({ address: r.address, family: r.type === 'AAAA' ? 6 : 4 }))
      .sort((a, b) => b.family - a.family);

    if (options.all === true) {
      return cb(null, hosts);
    }

    return cb(null, hosts[0].address, hosts[0].family);
  });
}

function createDnsServer(ipv6Addr, ipv4Addr, cb) {
  // Create a DNS server which replies with a AAAA and a A record for the same host
  const socket = dgram.createSocket('udp4');

  socket.on('message', common.mustCall((msg, { address, port }) => {
    const parsed = parseDNSPacket(msg);
    const domain = parsed.questions[0].domain;
    assert.strictEqual(domain, 'example.org');

    socket.send(writeDNSPacket({
      id: parsed.id,
      questions: parsed.questions,
      answers: [
        { type: 'AAAA', address: ipv6Addr, ttl: 123, domain: 'example.org' },
        { type: 'A', address: ipv4Addr, ttl: 123, domain: 'example.org' },
      ]
    }), port, address);
  }));

  socket.bind(0, () => {
    const resolver = new Resolver();
    resolver.setServers([`127.0.0.1:${socket.address().port}`]);

    cb({ dnsServer: socket, lookup: _lookup.bind(null, resolver) });
  });
}

// Test that IPV4 is reached if IPV6 is not reachable
{
  createDnsServer('::1', '127.0.0.1', common.mustCall(function({ dnsServer, lookup }) {
    const ipv4Server = createServer(common.mustCall((_, res) => {
      res.writeHead(200, { Connection: 'close' });
      res.end('response-ipv4');
    }));

    ipv4Server.listen(0, '127.0.0.1', common.mustCall(() => {
      request(
        `http://example.org:${ipv4Server.address().port}/`,
        {
          lookup,
          autoSelectFamily: true,
          autoSelectFamilyAttemptTimeout
        },
        (res) => {
          assert.strictEqual(res.statusCode, 200);
          res.setEncoding('utf-8');

          let response = '';

          res.on('data', (chunk) => {
            response += chunk;
          });

          res.on('end', common.mustCall(() => {
            assert.strictEqual(response, 'response-ipv4');
            ipv4Server.close();
            dnsServer.close();
          }));
        }
      ).end();
    }));
  }));
}

// Test that IPV4 is NOT reached if IPV6 is reachable
if (common.hasIPv6) {
  createDnsServer('::1', '127.0.0.1', common.mustCall(function({ dnsServer, lookup }) {
    const ipv4Server = createServer(common.mustNotCall((_, res) => {
      res.writeHead(200, { Connection: 'close' });
      res.end('response-ipv4');
    }));

    const ipv6Server = createServer(common.mustCall((_, res) => {
      res.writeHead(200, { Connection: 'close' });
      res.end('response-ipv6');
    }));

    ipv4Server.listen(0, '127.0.0.1', common.mustCall(() => {
      const port = ipv4Server.address().port;

      ipv6Server.listen(port, '::1', common.mustCall(() => {
        request(
          `http://example.org:${ipv4Server.address().port}/`,
          {
            lookup,
            autoSelectFamily: true,
            autoSelectFamilyAttemptTimeout,
          },
          (res) => {
            assert.strictEqual(res.statusCode, 200);
            res.setEncoding('utf-8');

            let response = '';

            res.on('data', (chunk) => {
              response += chunk;
            });

            res.on('end', common.mustCall(() => {
              assert.strictEqual(response, 'response-ipv6');
              ipv4Server.close();
              ipv6Server.close();
              dnsServer.close();
            }));
          }
        ).end();
      }));
    }));
  }));
}
