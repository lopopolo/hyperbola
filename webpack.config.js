const path = require("path");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const WebappWebpackPlugin = require("webapp-webpack-plugin");

const plugins = () => [
  new MiniCssExtractPlugin({
    filename: "[name].bundle.css"
  }),
  new WebappWebpackPlugin({
    logo: path.resolve(__dirname, "src/logo.svg"),
    prefix: "",
    cache: false
  })
];

module.exports = {
  entry: "main",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "[name].bundle.js"
  },
  resolve: {
    modules: ["node_modules", "src"],
    extensions: [".js"]
  },
  plugins: plugins(),
  optimization: {
    concatenateModules: true,
    minimizer: [
      new UglifyJsPlugin({
        cache: true,
        parallel: true
      }),
      new OptimizeCSSAssetsPlugin({})
    ]
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader"
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: "css-loader",
            options: {
              minimize: true
            }
          },
          "sass-loader"
        ]
      },
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: "css-loader",
            options: {
              minimize: true
            }
          }
        ]
      },
      {
        test: /\.(jpe?g|png|ttf|eot|woff(2)?)(\?[a-z0-9=&.]+)?$/,
        use: {
          loader: "base64-inline-loader",
          options: {
            limit: 2048,
            name: "[name].[ext]"
          }
        }
      },
      {
        test: /\.(svg)(\?[a-z0-9=&.]+)?$/,
        use: ["base64-inline-loader", "svgo-loader"]
      }
    ]
  }
};
