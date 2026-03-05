Hackathons
==========

DeFiPy has been built and showcased in multiple hackathons focused on DeFi analytics,
simulation, and live on-chain modeling.

ETHDenver 2024
--------------

**Project:** DeFi Paper Trading — Live Modeling Tool (0x Price API)

A Python-based DeFi simulation and modeling toolkit for paper trading LP positions
using live mainnet data from the **0x Price API**, plus a live dashboard UI. 

**Award / Recognition**
  - **0x: Third Prize** (ETHDenver 2024 sponsor prize). 
  - Received Quadratic Voting matching support during ETHDenver 2024.

**What it does (high level)**
  - Select a live liquidity pool using 0x price feeds
  - Simulate trades against the pool (paper trading)
  - Explore parameters (max swap size, bias, LP profitability)
  - Visualize results via a live dashboard 

**Tech**
  - Python, SciPy, Bokeh, DeFiPy, 0x Price API 

.. image:: img/ethdenver_2024_0x_judges.png
   :width: 85%
   :align: center
**DeFiPy presented at ETHDenver 2024 with the 0x judging panel**

🔗 `Link to project page  >> <hhttps://devfolio.co/projects/defi-paper-trading-live-modeling-tool-with-x-5d78>`_

---

ETHDam 2024 (ETH Amsterdam)
---------------------------

**Project:** DeFiPy (ETHDam 2024)

Hackathon entry describing DeFiPy as an open-source Python package for DeFi modeling,
including Uniswap v2 refactor and a live dashboard driven by 0x price feeds. :contentReference[oaicite:8]{index=8}

**Track**
  - ETHDam — Security Track :contentReference[oaicite:9]{index=9}

**What was added for ETHDam (“ETH Amsterdam Additions”)**
  - Support for a premium 0x API key (JumpStart program) stored privately on the backend,
    while allowing users who fork the repo to provide their own API key via `.env`. 
  - Supabase integration for user records + email login. 
  - Planned rollout of these additions to the live dashboard after cleanup. 

🔗 `Link to project page >> <hhttps://taikai.network/cryptocanal/hackathons/ethdam2024/projects/clux0p0rv00lmz301nq7yw7t1/idea>`_
