# Minecraft Mod Downloader

## Note: This is still in pre-release, you might find bugs n stuff, sorry for anything

A Python script to download Minecraft mods from Modrinth and Curseforge automatically.
Supports single mod downloads, batch downloads from a list, and dependency resolution (Auto download still WIP (i dont even know if i will actually finish it lmao))
Comes with free spaghetti code

## Disclaimer

We're not responsible for any damage caused by this package, including but not limited to:

- Brain damage
- Emotional Damage
- PseudoComa
- Spontaneous combustion
- High doses of radiation poisoning
- Deep Root Disease
- Spaghettification
- Non-Existence
- Enlightment
- *Death*

### Requirements

- Python 3.11 or later
- Pip

## How to use

### Installation

- Download the tar.gz from this repo
- Run "pip install [path to the tarball]"

### Setting up

- go to [The official CurseForge dev console](https://console.curseforge.com/#%2Fapi-keys) to get a curseforge api key
- Open your cmd, and type "mcmm -c cf-api-key [the key you received]"
- As simple as that

### Usage

General usage: Use "mcmm" as a prefix to run a command, then add the arguments (e.g: -m [mod link], -g 1.20.1, etc)

#### Basic downloads

- Open the cmd/powershell in the directory you want to output the files
- Type "mcmm -m [Mod Link] [other parameters]" for basic, single mod download from a url
- Type "mcmm -ml [Link1, Link2, ...] [other parameters]" for multiple downloads, separating each url with a space
- Type "mcmm -mlt [Path to the txt] [other parameters]" to download multiple mods at the same time using a txt file with a single mod url per line

#### Mod Filtering Parameters

- "-g [game version]" to specify a game version
- "-l [mod loaders]" to specify a single or multiple mod loaders (defaults to forge and neoforge)
- "-r [version type]" **DEPRECATED:** to specify the type of version to the mod (Release, Beta, Alpha). Note that this parameter is broken and may not work with CurseForge links.

#### Some extra commands

- "-o" optional output directory, always defaults to the folder you're in
- "-c" set configurations, only has "cf-api-key" yet
- "-h" or "--help" prints all commands with a detailed description (and aliases/long versions)

#### **WIP:** Dependency resolution

- "-rd" **Not implemented:** Attempts to resolve any cached missing dependencies.
- "-bl" **Not implemented:** Automatically blacklists any dependencies removed by -rw
- "-rw" **Implemented:** Opens the missing dependencies file for manual review and editing

### Output

The script create two folders in the output directory:

- "mods", which has the downloaded mods
- "results", which holds some txt files with the results

The txts in the results folder can be:

- "Successful_downloads.txt", stores the name of every successfully downloaded mod
- "Failed_downloads.txt", stores the modlinks and the cause of every failed mod download
- "MissingDependencies.txt", store the name of any missing dependency in case the script detects any, does not auto donwload yet (might implement, but still not sure)

## License and Copyright Information

### Copyright

This software is licensed under the MIT License
