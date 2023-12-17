![status: active](https://img.shields.io/badge/status-active-green.svg)
![status: release](https://img.shields.io/badge/release-0.1.0-red.svg)
![status: branch](https://img.shields.io/badge/branch-master-lightgrey.svg)

<div style="text-align: right"> 
    <a href="https://www.buymeacoffee.com/mattintech" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</div>


# KnoxTokenLibary-Python

**This is not an offical Samsung library or repository**

This is a python rewrite of the knox-token-library-js library written by Samsung.  The following code was used to build this project. https://www.npmjs.com/package/knox-token-library-js?activeTab=readme

The prerequesits for this library are: 
```
pip install pycryptodome "pyjwt[crypto]"
```

## Usage
Tutorial for authentication can be found here: https://docs.samsungknox.com/dev/knox-cloud-authentication/tutorial/tutorial-for-customers-generate-access-token/. 

You can also leverage the KnoxAccessToken.py & test_KmeApi.py examples that show successful authetnication to the Knox Mobile Enrollment ('KME') api.

The example leverages a keys.json which is obtained using the SamsungKnox.com portal - view the Samsung tutorial for more details. 
The example also leverages clientId.json which includes the clientIds 

```
{
    "kme": "",
    "kc": "",
    "ke1": "",
    "kai": ""
}
```

## Build & Install
In order to install the KTL you must build 

```
python setup.py sdist bdist_wheel
pip install .
```

Note - the above requires prerequesit wheel

```
pip install wheel
```

