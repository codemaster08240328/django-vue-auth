var hotClient = require("webpack-hot-middleware/client?noInfo=true&reload=true&path=http://localhost:8080/__webpack_hmr");
var devMiddleware = require("webpack-dev-middleware")(compiler, {
  headers: {
    "Access-Control-Allow-Origin": "*"
  }
  // ...
});
