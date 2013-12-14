# Inspired by http://sleepycoders.blogspot.de/2013/03/sharing-travis-ci-generated-files.html?_escaped_fragment_#!
if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
  echo -e "Starting to update gh-pages\n"

  echo `ls -al`

  #copy data we're interested in to other place
  cp -R .build $HOME/build

  #go to home and setup git
  cd $HOME
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis"

  #using token clone gh-pages branch
  git clone --quiet --branch=gh-pages https://${GH_TOKEN}@github.com/Ookami86/event-sourcing-in-practice.git  gh-pages

  #go into diractory and copy data we're interested in to that directory
  cd gh-pages
  cp -Rf $HOME/build/* .

  #add, commit and push files
  git add -f .
  git commit -m "Travis build $TRAVIS_BUILD_NUMBER pushed to gh-pages"
  git push -fq origin gh-pages 

  echo -e "Done publishing to gh-pages.\n"
fi
