const path = require("path");
const glob = require("glob-all");
const webpack = require("webpack");
const ExtractTextPlugin = require("extract-text-webpack-plugin");

const extractCSS = new ExtractTextPlugin({ filename: "[name].bundle.css" });

module.exports = {
  entry: "main",
  output: {
    path: path.resolve(__dirname, "./dist"),
    filename: "[name].bundle.js",
  },
  resolve: {
    modules: ["node_modules", "src"],
    extensions: [".js"]
  },
  plugins: [
    extractCSS,
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false,
      },
      output: {
        comments: false,
      },
    }),
  ],
  module: {
    rules: [
      {
        enforce: "pre",
        test: /\.jsx?$/,
        loader: "eslint-loader",
        exclude: /node_modules/,
        options: {
          eslint: {
            failOnWarning: false,
            failOnError: true
          },
        },
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader"
      },
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: "css-loader!postcss-loader",
        }),
      },
      {
        test: /\.scss$/,
        use: extractCSS.extract({
          fallback: "style-loader",
          use: "css-loader!postcss-loader!sass-loader",
        }),
      },
      {
        test: /\.(jpe?g|png|ttf|eot|svg|woff(2)?)(\?[a-z0-9=&.]+)?$/,
        use: "base64-inline-loader?limit=2000&name=[name].[ext]",
      },
    ],
  },
};
