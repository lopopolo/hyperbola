const path = require("path");
const CleanWebpackPlugin = require("clean-webpack-plugin");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const WebappWebpackPlugin = require("webapp-webpack-plugin");
const FileManagerPlugin = require("filemanager-webpack-plugin");

const plugins = () => [
  new CleanWebpackPlugin(
    ["./dist/*", "./document-root/**/*.ico", "./document-root/**/*.png"],
    {
      exclude: [".gitignore"]
    }
  ),
  new MiniCssExtractPlugin({
    filename: "[name].bundle.css"
  }),
  new WebappWebpackPlugin({
    logo: "./src/img/logo.favicon.svg",
    prefix: "icons/",
    cache: false,
    // which icons should be generated (see https://github.com/haydenbleasel/favicons#usage)
    favicons: {
      appName: "hyperbola",
      icons: {
        android: false,
        appleIcon: true,
        appleStartup: false,
        coast: false,
        favicons: true,
        firefox: false,
        opengraph: false,
        twitter: false,
        yandex: false,
        windows: false
      }
    }
  }),
  new FileManagerPlugin({
    onEnd: [
      {
        move: [
          {
            source: "./dist/icons/favicon.ico",
            destination: "./document-root/favicon.ico"
          },
          {
            source: "./dist/icons/apple-touch-icon.png",
            destination: "./document-root/apple-touch-icon.png"
          }
        ]
      },
      {
        delete: ["./dist/icons"]
      }
    ]
  })
];

module.exports = {
  entry: "main",
  output: {
    path: path.resolve(__dirname, "./dist"),
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
            limit: 2000,
            name: "[name].[ext]"
          }
        }
      },
      {
        test: /\.(svg)(\?[a-z0-9=&.]+)?$/,
        use: [
          {
            loader: "base64-inline-loader",
            options: {
              limit: 2000,
              name: "[name].[ext]"
            }
          },
          {
            loader: "svgo-loader"
          }
        ]
      }
    ]
  }
};
