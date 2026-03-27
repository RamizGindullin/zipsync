This is a mirror to `stgatilov/zipsync`. The goal is to make the project compile on MacOS (as a first, albeit small, step to make The Dark Mod ported). The current version requires installation of Conan (see [here](https://docs.conan.io/2/installation.html])).


## How to compile

To compile on MacOS you need to open the Terminal:

```
cd /path/to/zipsync
./conan_build.sh
```

The compiled files will be saved in `/path/to/zipsync/build/RelWithDebInfo`

## Conan compatibility
Conan doesn't currently know about Apple Clang 21 (shipped with Xcode 16.x). You need to add it manually:
```
bash
nano ~/.conan2/settings.yml
```
Find the `apple-clang` version list and add "21" to the end:

```
apple-clang:
    version: ["5.0", "5.1", "6.0", ..., "17", "17.0", "21"]
```

Save the file.


## How to use zipsync

In Terminal (version 2.14):
```
cd /path/to/zipsync/build/RelWithDebInfo
```

```
BASE=http://tdm.frydrych.org/mirror/zipsync
./zipsync update --clean \
  -r <path to your installation> \
  -t $BASE/release/release214_from_release213/manifest.iniz \
  -p $BASE/release/release213_from_release212/manifest.iniz \
  -p $BASE/release/release212_from_release211/manifest.iniz \
  -p $BASE/release/release211_from_release210/manifest.iniz \
  -p $BASE/release/release210_from_release209/manifest.iniz \
  -p $BASE/release/release209_from_release208/manifest.iniz \
  -p $BASE/release/release208_from_release207/manifest.iniz \
  -p $BASE/release/release207_from_release206/manifest.iniz \
  -p $BASE/release/release206_from_release205/manifest.iniz \
  -p $BASE/release/release205_from_release204/manifest.iniz \
  -p $BASE/release/release204_from_release203/manifest.iniz \
  -p $BASE/release/release203_from_release202/manifest.iniz \
  -p $BASE/release/release202_from_release201/manifest.iniz \
  -p $BASE/release/release201_from_release200/manifest.iniz \
  -p $BASE/release/release200/manifest.iniz
```

This will allow you to download the content of TDM into your folder.
