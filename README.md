# UNIVERSAL LINUX APP
Apps format for UNIX-like OS. You must have bash-like shell to run it.

## Commands
- `./main.py -u <app_name (without '.ula')>` - unpacks package.
- `./main.py -r <app_name (without '.ula')>` - runs unpacked app.
- `./main.py -ur <app_name (without '.ula')>` - unpacks package then runs it.
- `./main.py -i <app_name (without '.ula')>` - gives information about package.

## How to create `.ula` file
Create `.tar` file and rename it to `.ula`. `.ula` file must contain `source` folder, `package.json` and `start.sh` files.

<hr>

### `source`
This folder must contain your executable file (that can run in bash-like shells).
For example:
<br>
`script.sh`
```sh
#!/usr/bin/bash
echo "Hello, World!"
```

<hr>

### `package.json`
Information of your package.
```JSON
{
    "name": "ExmpleApp",
    "version": "1.0",
    "author": "author",
    "format-version": "0.1" // It's a test option, but required!
}
```

<hr>

### `start.sh`
Runs your executable from `source` folder.
```sh
#!/usr/bin/bash
sh ./source/test.sh
```
