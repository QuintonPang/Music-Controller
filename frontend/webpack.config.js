const path = require("path");


const webpack = require("webpack");


module.exports = {

	//file of entry point

	entry: "./src/index.js", 

	output: { 

		//location to bundle and place file
		path: path.resolve(__dirname, "./static/frontend"),

		filename: "[name].js",

	},


	module: { 

		rules: [

			{
				test: /\.js$/,

				exclude: /node_modules/, 

				use: { 

					loader: "babel-loader",
			
				}, 
			},
		],

	},

	optimization: {

		//make files smaller when bundling

		minimize: true,

	}, plugins: [ 

		new webpack.DefinePlugin({ 

			"process.env": { 


				// This has effect on the react lib size 

				NODE_ENV:JSON.stringify("development"), 


	
			},



		}),

	],

};
