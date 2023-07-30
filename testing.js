const fs = require('fs');

fs.readFile('/home/rohit/Documents/Learning/tempelates/invoice.html', 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    
    var result = data.replace('memberName', 'Rohit Raj');
    result = result.replace('inVoiceDate' , "12/2312/13212");
    result = result.replace('UPI' , "CARD");
  
    fs.writeFile(`/home/rohit/Documents/Learning/docs/invoice - gi.html`, result, 'utf8', function (err) {
       if (err) return console.log(err);
    });
  });