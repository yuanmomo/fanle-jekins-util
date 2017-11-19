# Jenkins-util
##### No longer rely on the browser to open jenkins, just a few word commands; also provid the alfred-workflow

### Dependencies

pip2 install jenkinsapi   
pip2 install jenkins    

brew install jq
brew install wget

### Config Your Jenkins

```
{
  "jenkins-url": "http://192.168.1.232:8080/jenkins(your jenkins url)",
  "username": "test(your username)",
  "password": "test(your password)",
  ......
  "zip-download-url": "http://192.168.1.232/download/zip/(your source download url)",
  ......
  "majiang-desktop-path":"/Applications/majiang-desptop.app/Contents/Resources(your destination dir)"
}
```
