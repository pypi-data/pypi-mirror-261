# LibRay 1.0.0 Specification

**Note**
This specification has not been implemented yet.

**Note**
Work in progress.

## User interaction

Here is a flow diagram to explain the different ways a user can interact with LibRay:

![LiBray flow][flow]

As you can see there are three main routes:

1. The user has a key (in hex)
2. The user has an .ird
3. The user has nothing

It is assumed that no. 3 is the most common way to use LibRay, simply give it your .iso file and let LibRay decrypt it.


## Database

LiBray bundles a database containing two tables:

- ird: containing parsed data from various .ird dumps
- redump: containing parsed data from redump

![LibRay DB tables][tables]


## Dependencies

- crypto: `pycryptodomex`
- progressbar: `tqdm`
- http/https: `requests`
- html: `beautifulsoup4`

In previous versions there were problems where dependencies interfered with eachother (notably, `crypto` vs `pycrypto` vs `pycryptodome`), so 1.0.0 and above uses `pycryptodomex` which is standalone from the previously mentioned packages.

## Packaging

- [Poetry](https://python-poetry.org/)





[flow]: flow.png "LibRay user interaction flowchart"
[tables]: tables.png "LibRay database tables"

