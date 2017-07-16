const path = require("path");
const glob = require("glob-all");
const webpack = require("webpack");
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const PurifyCSSPlugin = require("purifycss-webpack");

module.exports = {
    entry: {
        main: ["main", "hyperbola.browser"],
    },
    output: {
        path: path.resolve(__dirname, "./dist"),
        filename: "[name].bundle.js",
    },
    resolve: {
        modules: ["node_modules", "src"],
        extensions: [".js"]
    },
    plugins: [
        new webpack.DefinePlugin({
            "process.env.NODE_ENV": JSON.stringify("production")
        }),
        new ExtractTextPlugin("[name].bundle.css"),
        new PurifyCSSPlugin({
            // Give paths to parse for rules. These should be absolute!
            paths: glob.sync([
                path.join(__dirname, "app/hyperbola/templates/*.html"),
                path.join(__dirname, "app/hyperbola/*/templates/*.html"),
            ]),
            minimize: true,
        }),
        new webpack.optimize.ModuleConcatenationPlugin(),
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
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "babel-loader"
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: "css-loader",
                }),
            },
            {
                test: /\.(jpe?g|png|ttf|eot|woff(2)?)(\?[a-z0-9=&.]+)?$/,
                use: {
                    loader: "base64-inline-loader",
                    options: {
                        limit: 2000,
                        name: "[name].[ext]",
                    },
                },
            },
            {
                test: /\.(svg)(\?[a-z0-9=&.]+)?$/,
                use: [
                    {
                        loader: "base64-inline-loader",
                        options: {
                            limit: 2000,
                            name: "[name].[ext]",
                        },
                    },
                    {
                        loader: "svgo-loader",
                        options: {
                            plugins: [
                                {removeTitle: true},
                                {convertColors: {shorthex: false}},
                                {convertPathData: false}
                            ]
                        }
                    },
                ],
            },
        ],
    },
};
