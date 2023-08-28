const Enquiry = require('../models/enquiries.model');
const moment = require('moment');



const saveEnquiryData = async (reqBody, res) => {
	try {
		let enquiry = new Enquiry(
			{
				name: reqBody.name,
				address: reqBody.address,
				postalCode: reqBody.postalCode,
				phoneNumber: reqBody.phoneNumber,
				email: reqBody.email,
				gender: reqBody.gender,
				maritalStatus: reqBody.maritalStatus,
				reasonToJoin: reqBody.reasonToJoin,
				visitedAt: moment().format("D MMMM YYYY"),
			});
		enquiry.save()
	}
	catch (err) {
		console.log(err);
	}
}


const readEnquiries = async (req, res) => {
	try {
		// console.log('....................2................', req.query)
		// const query = {};
		// if(req.query.keyword)
		// {
		//     query.$or = [
		//         { "name": { $regex: req.query.keyword, $options: 'i'}}
		//     ]
		// }

		// const enquiries = await Enquiry.find(query)
		// .skip(0)
		// .limit(2)
		// .sort( { _id : -1 })
		// console.log(enquiries);
		// return res.status(200).send({
		//     message: 'Enquiry Data Fetched',
		//     data: enquiries
		// })
		let query = [

		];

		if (req.query.keyword && req.query.keyword != '') {
			query.push({
				$match: {
					$or: [
						{
							name: { $regex: req.query.keyword }
						}
					]
				}
			});
		}

		if (req.query.sortOrder) {

			query.push({
				$sort: { _id: 1 }
			});
		} else {
			query.push({
				$sort: { _id: -1 }
			});
		}



		let total = await Enquiry.countDocuments(query);
		let page = (req.query.page) ? parseInt(req.query.page) : 1;
		let perPage = (req.query.perPage) ? parseInt(req.query.perPage) : 10;
		let skip = (page - 1) * perPage;
		query.push({
			$skip: skip,
		});
		query.push({
			$limit: perPage,
		});



		let enquiries = await Enquiry.aggregate(query);
		return res.send({
			enquiries
		});

	}
	catch (err) {

	}

}


module.exports = { saveEnquiryData, readEnquiries }