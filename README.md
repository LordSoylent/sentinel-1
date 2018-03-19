# SunCoin (SUN) - Masternode Sentinel

First Global CO2 Neutral Blockchain Network

With focus on emission neutral mining and an CO2 initiative fund, SunCoin  is the thought leader in creating a sustainable distributed ledger system awareness and offer working solution for decarbonizing the market. With your help, SunCoin will balance out impact on our environment and provide new ways powering the future of crypto finance and distributed ledger systems.

**Info:** SunCoin is a proud fork of Dash. Kudos to the Dash team for the hard work and creating the technical foundation for a community driven project as SunCoin.

This guide covers installing Sentinel onto an Masternode in Ubuntu 14.04 or 16.04.

## Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Make sure the local SunCoin daemon is running:

    $ suncoin-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/suncoin-network/sentinel.git
    $ cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1
    
For debugging you can use:    
    
    * * * * * cd /home/sentinel && SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py --bypass-schedule >> sentinel.log 2>&1
    
## Configuration

An alternative (non-default) path to the `suncoin.conf` file can be specified in `sentinel.conf`:

    suncoin_conf=/path/to/suncoin.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py
