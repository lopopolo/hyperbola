const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const TerserPlugin = require("terser-webpack-plugin");

const plugins = [new MiniCssExtractPlugin()];

module.exports = {
  context: path.resolve(__dirname),
  output: {
    path: path.resolve(__dirname, "dist")
  },
  plugins,
  optimization: {
    minimize: true,
    minimizer: [new TerserPlugin(), new OptimizeCSSAssetsPlugin()]
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader"
      },
      {
        test: /\.s?css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
      },
      {
        test: new RegExp(path.resolve(__dirname, "src", "assets")),
        use: {
          loader: "file-loader",
          options: {
            name: "[name].[ext]"
          }
        }
      },
      {
        test: /\.(png|jpe?g|gif)$/i,
        exclude: new RegExp(path.resolve(__dirname, "src", "assets")),
        use: {
          loader: "url-loader",
          options: {
            limit: 8192
          }
        }
      },
      {
        test: /\.svg$/i,
        use: ["file-loader", "svgo-loader"]
      }
    ]
  }
};
