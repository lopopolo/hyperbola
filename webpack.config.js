const path = require("path");
const glob = require("glob");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const PurgecssPlugin = require("purgecss-webpack-plugin");
const WebappWebpackPlugin = require("webapp-webpack-plugin");

const plugins = [
  new MiniCssExtractPlugin(),
  new PurgecssPlugin({
    paths: glob.sync(
      `${path.resolve(__dirname)}/hyperbola/**/templates/*.html`,
      { nodir: true }
    ),
    whitelistPatterns: [/^code$/, /mx-auto/, /d-block/],
    whitelistPatternsChildren: [/^syntax$/]
  }),
  new WebappWebpackPlugin({
    logo: path.resolve(__dirname, "src/logo.svg"),
    prefix: "",
    cache: false
  })
];

module.exports = {
  context: path.resolve(__dirname),
  output: {
    path: path.resolve(__dirname, "dist")
  },
  plugins,
  optimization: {
    minimizer: [
      new UglifyJsPlugin({
        cache: true,
        parallel: true
      }),
      new OptimizeCSSAssetsPlugin()
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
        test: /\.s?css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
      },
      {
        test: /\.(png|jpe?g|gif)$/,
        use: {
          loader: "url-loader",
          options: {
            limit: 8192
          }
        }
      },
      {
        test: /\.svg$/,
        use: ["svg-url-loader", "svgo-loader"]
      }
    ]
  }
};
