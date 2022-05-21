heroku buildpacks:set https://github.com/heroku/heroku-geo-buildpack.git
https://elements.heroku.com/buildpacks/heroku/heroku-geo-buildpack

$ heroku buildpacks
=== Buildpack URLs
1. https://github.com/heroku/heroku-geo-buildpack.git
2. heroku/python


heroku create --buildpack https://github.com/heroku/heroku-geo-buildpack.git