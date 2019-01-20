# Bitmark Node Documentation

[ [English](#introduction) | [中文](#簡介) ]

## Introduction

The [Bitmark](https://bitmark.com) node software enables any computer on the Internet to join the Bitmark network as a fully-validating peer. Unlike conventional property systems that rely on a handful of trusted government officials to act as centralized gatekeepers, the Bitmark blockchain is an open and transparent property system that is strengthened through the active participation of anyone on the Internet. The integrity of Bitmark’s open-source blockchain is ensured by a peer-to-peer network of voluntary participants running the Bitmark node software. These participants are incentivized to participate in verifying Bitmark property transactions through the possibility of winning monetary and property rewards.

The Bitmark blockchain is an independent chain, optimized for storing property titles, or *bitmarks*, and does not have its own internal currency (transaction fees are in bitcoin or litecoin). The peer-to-peer network is written in [Go](https://golang.org) and uses the [ZeroMQ distributed messaging library](http://zeromq.org). Consensus is secured using the [Argon2](https://github.com/P-H-C/phc-winner-argon2) hashing algorithm as proof-of-work.

***Read our [Governance policy](https://bitmark.com/governance-policy) to learn how to contribute to this project**

## Suported Platforms

The Bitmark node software is distributed as a standalone [Docker container](https://www.docker.com/what-container), which supports easy installation on all major platforms including:

- **desktop devices**, such as [Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac) and [Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)
- **Linux servers**, such as [CentOS](https://store.docker.com/editions/community/docker-ce-server-centos), [Debian](https://store.docker.com/editions/community/docker-ce-server-debian), [Fedora](https://store.docker.com/editions/community/docker-ce-server-fedora), and [Ubuntu](https://store.docker.com/editions/community/docker-ce-server-ubuntu)
- **cloud providers**, such as [AWS](https://store.docker.com/editions/community/docker-ce-aws) and [Azure](https://store.docker.com/editions/community/docker-ce-azure)


## Contents

The Bitmark node consists of the following software programs:

 - **bitmarkd** — the main program for verifying and recording transactions in the Bitmark blockchain [(view source code on GitHub)](https://github.com/bitmark-inc/bitmarkd/tree/master/command/bitmarkd)
 - **recorderd** — an auxillary application for computing the Bitmark proof-of-work algorithm that allows nodes to compete to win blocks on the Bitmark blockchain [(view source code on GitHub)](https://github.com/bitmark-inc/bitmarkd/tree/master/command/recorderd)
 - **bitmark-wallet** — an integrated cryptocurrency wallet for receiving Bitcoin and Litecoin payments for won blocks [(view source code on GitHub)](https://github.com/bitmark-inc/bitmark-wallet)
 - **bitmark-cli** — a command line interface to `bitmarkd` [(view source code on GitHub)](https://github.com/bitmark-inc/bitmarkd/tree/master/command/bitmark-cli)
 - **bitmark-webui** — a web-based user interface to monitor and configure the Bitmark node via a web browser

## Installation

**To install the Bitmark node software, please complete the following 4 steps:**

### 1. Install Docker

The Bitmark node software is distributed as a standalone [Docker container](https://www.docker.com/what-container) which requires you to first install Docker for your operating system:


- [Get Docker for MacOS](https://store.docker.com/editions/community/docker-ce-desktop-mac)
- [Get Docker for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)
- [Get Docker for CentOS](https://store.docker.com/editions/community/docker-ce-server-centos)
- [Get Docker for Debian](https://store.docker.com/editions/community/docker-ce-server-debian)
- [Get Docker for Fedora](https://store.docker.com/editions/community/docker-ce-server-fedora)
- [Get Docker for Ubuntu](https://store.docker.com/editions/community/docker-ce-server-ubuntu)
- [Get Docker for AWS](https://store.docker.com/editions/community/docker-ce-aws)
- [Get Docker for Azure](https://store.docker.com/editions/community/docker-ce-azure)

### 2. Download the Bitmark Node

After successfully installing Docker, you can download the Bitmark node software. To do so, first open a command-line terminal or shell application, such as Terminal on the Mac or `cmd.exe` on Windows. Then enter the following command to download the Bitmark node software:

```
docker pull bitmark/bitmark-node
```


After entering the pull command, the download sequence should begin in the terminal. You will receive the following message after the download is completed successfully:

```
Status: Downloaded newer image for bitmark/bitmark-node:latest
```


### 3. Run Bitmark Node

After the Bitmark node software has successfully downloaded, copy and paste the following command into the command-line terminal to run the Bitmark node:

```
docker run -d --name bitmarkNode -p 9980:9980 \
-p 2136:2136 -p 2130:2130 \
-e PUBLIC_IP=[YOUR_PUBLIC_IP] \
-v $HOME/bitmark-node-data/db:/.config/bitmark-node/db \
-v $HOME/bitmark-node-data/data:/.config/bitmark-node/bitmarkd/bitmark/data \
-v $HOME/bitmark-node-data/data-test:/.config/bitmark-node/bitmarkd/testing/data \
bitmark/bitmark-node
```

Please remember to replace `[YOUR_PUBLIC_IP]` to your node public ip. Once the Bitmark node has successfully started, it will return a 64-character hexidecimal string that represents the Bitmark node's Docker container ID, such as:

```
dc78231837f2d320f24ed70c9f8c431abf52e7556bbdec257546f3acdbda5cd2
```


When the Bitmark node software is started up for the first time, it will generate a Bitmark account for you, including your public and private keypairs.

For an explanation of each of the above `run` command options, please enter the following command into the terminal:

```
docker run --help
 ```



### 4. Start Services in Web Interface

The Bitmark node includes a web-based user interface to monitor and control the Bitmark node within a web browser. After running the Bitmark node in step 3, you should launch the web UI to start the `bitmarkd` and optional `recorderd` programs.

On most computer systems, the web UI can be accessed on port `9980` of the `localhost` address (`127.0.0.1`) by clicking the following link:

> [http://127.0.0.1:9980](http://127.0.0.1:9980).

After loading web UI, you should use it to start the two main Bitmark node software programs:

1. `bitmarkd` — responsible for verifying Bitmark transactions and recording them in the Bitmark blockchain (required for all Bitmark nodes)
2. `recorderd` — required for solving the Bitmark blockchain's proof-of-work algorithm, which qualifies nodes to win blocks and receive monetary compensation (optional)

After starting the `bitmarkd` node for the first time, the node will go through an initial `Resynchronizing` phase in which a copy of the current Bitmark blockchain will be downloaded to your Bitmark node. Once the blockchain resynchronization has completed, your Bitmark node will begin verifying and recording transactions for the current block.


## Configuration Options

### Current Blockchain

The Bitmark node allows participants to verify and record transactions on two different Bitmark blockchains:

- `bitmark` — the official version of the Bitmark blockchain
- `testing` — a `testnet` version of the blockchain used solely for development testing

Node participants can select which blockchain they are currently working on via the web UI. Note that switching to a different blockchain will require you to restart the `bitmarkd` and `recorderd` programs in the web UI for the new blockchain.

The Bitmark system offers monetary rewards to block winners for both the `bitmark` and `testing` blockchains.

### Payment Addresses

Bitmark node participants running both `bitmarkd` and `recorderd` are awarded monetary payments for winning blocks on both the `bitmark` and `testing` blockchains. These payments are delivered as either bitcoin or litecoin payments (depending on current cryptocurrency prices and confirmation times) and are delivered to a node's designated bitcoin and litecoin payment addresses.

When the Bitmark node software is first started up, the installation program automatically generates default bitcoin and litecoin payment addresses. These payment addresses can be viewed and configured in the Bitmark node web UI.


### Docker Run Command Options

Various Bitmark node environmental settings, such as ports and IP addresses, can be configured using the Docker `run` command when running the Bitmark node from the command-line terminal:

```
docker run -d --name bitmarkNode -p 9980:9980 \
-p 2136:2136 -p 2130:2130 \
-e PUBLIC_IP=[YOUR_PUBLIC_IP] \
-v $HOME/bitmark-node-data/db:/.config/bitmark-node/db \
-v $HOME/bitmark-node-data/data:/.config/bitmark-node/bitmarkd/bitmark/data \
-v $HOME/bitmark-node-data/data-test:/.config/bitmark-node/bitmarkd/testing/data \
bitmark/bitmark-node
```

The following table describes the various configuration options for the Bitmark node `run` command:


| OPTION  | DEFAULT  | DESCRIPTION  |
|:---|:---|:---|
| `-name`  | `bitmarkNode` | Assigns a name to the Bitmark node Docker container. |
| `-p`  | `9980` | Web server port for web UI |
| `-p`  | `2136` | Port for connecting to other peer bitmarkd nodes |
| `-p`  | `2135` | Port for connecting to other peer bitmarkd nodes |
| `-p`  | `2130` | Port for Bitmark node [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) server |
| `-e`  | `PUBLIC_IP=[YOUR_PUBLIC_IP]` | Environment variable for register your public IP address |

### Docker Compose Settings

Participants familiar with [Docker Compose](https://docs.docker.com/compose/) can use the included `docker-compose.yml` file as an example for how to configure Bitmark node services.

Configurable options are:

  - Environments:
    - PUBLIC_IP: Your public IP address
  - Ports:
    - 2130: Port of RPC server
    - 2135 & 2136: Port of peering
    - 9980: Port of web server
    _(Note: Please make sure that you setup port forwarding with TCP in order to let others connect you via public network)_
  - Volumes:
    - /.config/bitmark-node/bitmarkd/bitmark/data - block data for `bitmark` blockchain
    - /.config/bitmark-node/bitmarkd/testing/data - block data for `testing` blockchain


## Updates

**To update the Bitmark node software, please complete the following 3 steps:**

### 1. Download Latest Node Version

To update your version of the Bitmark node software, open a command-line terminal or shell application, such as Terminal on the Mac or `cmd.exe` on Windows, then enter the following command to download the software update:

```
docker pull bitmark/bitmark-node
```


After entering the pull command, the download sequence should begin in the terminal. You will receive the following message after the download is completed successfully:

```
Status: Downloaded newer image for bitmark/bitmark-node:latest
```


### 2. Run Bitmark Node

After the software update has successfully downloaded, you need remove the previous container and start a new one via command-line terminal:

```
docker rm -f bitmarkNode
docker run -d --name bitmarkNode -p 9980:9980 \
-p 2136:2136 -p 2130:2130 \
-e PUBLIC_IP=[YOUR_PUBLIC_IP] \
-v $HOME/bitmark-node-data/db:/.config/bitmark-node/db \
-v $HOME/bitmark-node-data/data:/.config/bitmark-node/bitmarkd/bitmark/data \
-v $HOME/bitmark-node-data/data-test:/.config/bitmark-node/bitmarkd/testing/data \
bitmark/bitmark-node
```



### 3. Restart Services in Web Interface

Finally, restart the `bitmarkd` and optional `recorderd` programs via the web UI. On most computer systems, the web UI can be accessed on port `9980` of the `localhost` address (`127.0.0.1`) by clicking the following link:

> [http://127.0.0.1:9980](http://127.0.0.1:9980).

After loading web UI, you should use it to start the two main Bitmark node software programs:

1. `bitmarkd` — reponsible for verifying Bitmark transactions and recording them in the Bitmark blockchain (required for all Bitmark nodes)
2. `recorderd` — required for solving the Bitmark blockchain's proof-of-work algorithm, which qualifies nodes to win blocks and receive monetary compensation (optional)

After restarting the `bitmarkd` node for the first time, the node will go through an initial `Resynchronizing` phase in which a copy of the current Bitmark blockchain will be downloaded to your Bitmark node. Once the blockchain resynchronization has completed, your Bitmark node will begin verifying and recording transactions for the current block.


# Bitmark節點說明

## 簡介

[Bitmark](https://bitmark.com) 節點是一個讓一台連網的電腦可以加入 Bitmark 網路並且參與驗證的軟體。Bitmark 區塊鏈與傳統的資產系統不同的地方在於，傳統的資產系統是一種由一群被信任的官方人員所運作的集中式管理系統，而 Bitmark 區塊鏈是一個任何人都可以透過網路積極參與驗證強化的開放透明資產系統。Bitmark 開源區塊鏈的健全性是由一群自願參與運行 Bitmark 節點軟體的人們所構成的P2P網路來維繫，而自願參與驗證 Bitmark 資產交易的誘因為可能贏得以金錢或是資產形式的獎勵。

Bitmark 區塊鏈是專門為了資產所有權（稱為 *bitmark* ）所優化的一條獨立的鏈，其本身並不是一種貨幣（交易手續費是用 bitcoin 或 litecoin 支付）。P2P 網路是用 [Go](https://golang.org) 語言寫成，並且使用 [ZeroMQ 分散式訊息庫](http://zeromq.org)。共識是使用 [Argon2](https://github.com/P-H-C/phc-winner-argon2) 的雜湊演算法來作為工作量證明。

***請參閱我們的 [Governance policy](https://bitmark.com/governance-policy) 了解如何參與與貢獻這個計畫**

## 支援平台

Bitmark節點軟體是透過獨立運作的 [Docker container](https://www.docker.com/what-container) 來發布。Docker container 可支援各主要平台的簡易安裝：

- **桌上型電腦**，如 [Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac)或[Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)
- **Linux伺服器**，如 [CentOS](https://store.docker.com/editions/community/docker-ce-server-centos)、 [Debian](https://store.docker.com/editions/community/docker-ce-server-debian)、 [Fedora](https://store.docker.com/editions/community/docker-ce-server-fedora)及[Ubuntu](https://store.docker.com/editions/community/docker-ce-server-ubuntu)
- **雲端服務**，如 [AWS](https://store.docker.com/editions/community/docker-ce-aws) 及 [Azure](https://store.docker.com/editions/community/docker-ce-azure)

## 內容

Bitmark 節點由以下軟體程式所組成：

- **bitmarkd** - 用於 Bitmark 區塊鏈驗證以及紀錄交易的主程式。[(在 GitHub 上檢視原始碼)](https://github.com/bitmark-inc/bitmarkd/tree/master/command/bitmarkd)
- **recorderd** - 用於計算 Bitmark 工作量證明演算法的附屬程式，使一個節點可以在 Bitmark 區塊鏈上爭取贏得區塊。[(在 GitHub 上檢視原始碼)](https://github.com/bitmark-inc/bitmarkd/tree/master/command/recorderd)
- **bitmark-wallet** - 一個加密貨幣錢包，用來收取贏得區塊後以 bitcoin 或 litecoin 形式支付的獎勵。[(在 GitHub 上檢視原始碼)](https://github.com/bitmark-inc/bitmark-wallet)
- **bitmark-cli** - `bitmarkd`的命令列介面。[(在 GitHub上 檢視原始碼)](https://github.com/bitmark-inc/bitmarkd/tree/master/command/bitmark-cli)
- **bitmark-webui** - 透過網頁瀏覽器來檢視及控制 Bitmark 節點的使用者介面網頁。

## 安裝

**請依照以下四個步驟來完成安裝 Bitmark 節點軟體：**

### 一、安裝 Docker

Bitmark 節點軟體是透過獨立運作的 [Docker container](https://www.docker.com/what-container) 來發布。首先請在您的作業系統上安裝 Docker：


- [取得 Docker for MacOS](https://store.docker.com/editions/community/docker-ce-desktop-mac)
- [取得 Docker for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)
- [取得 Docker for CentOS](https://store.docker.com/editions/community/docker-ce-server-centos)
- [取得 Docker for Debian](https://store.docker.com/editions/community/docker-ce-server-debian)
- [取得 Docker for Fedora](https://store.docker.com/editions/community/docker-ce-server-fedora)
- [取得 Docker for Ubuntu](https://store.docker.com/editions/community/docker-ce-server-ubuntu)
- [取得 Docker for AWS](https://store.docker.com/editions/community/docker-ce-aws)
- [取得 Docker for Azure](https://store.docker.com/editions/community/docker-ce-azure)

### 二、下載 Bitmark 節點

成功安裝 Docker 之後，您就可以下載 Bitmark 節點了。請先開啟命令列終端機或是命令提示字元，例如在 Mac 上的 Terminal 或是在 Windows 上的`cmd.exe`。然後輸入以下的指令來下載 Bitmark 節點軟體：

```
docker pull bitmark/bitmark-node
```

輸入 pull 的指令之後，下載應該就會開始執行。成功下載完成後，您會收到以下訊息：

```
Status: Downloaded newer image for bitmark/bitmark-node:latest
```

### 三、執行 Bitmark 節點

成功下載 Bitmark 節點之後，複製並貼上以下的指令於在命令列終端機上以執行 Bitmark 節點：

```
docker run -d --name bitmarkNode -p 9980:9980 \
-p 2136:2136 -p 2130:2130 \
-e PUBLIC_IP=[YOUR_PUBLIC_IP] \
-v $HOME/bitmark-node-data/db:/.config/bitmark-node/db \
-v $HOME/bitmark-node-data/data:/.config/bitmark-node/bitmarkd/bitmark/data \
-v $HOME/bitmark-node-data/data-test:/.config/bitmark-node/bitmarkd/testing/data \
bitmark/bitmark-node
```

請注意將`[YOUR_PUBLIC_IP]`置換成節點的對外IP。一旦 Bitmark 節點成功的開始執行，它會回傳一個代表 Bitmark 節點的 Docker container ID 的64字的16進位字串，如：

```
dc78231837f2d320f24ed70c9f8c431abf52e7556bbdec257546f3acdbda5cd2
```


當 Bitmark 節點軟體第一次運行的時候，它會為您產生一個 Bitmark 帳號，其中包含您的公鑰與密鑰組。

如欲了解`run`指令的各種選項，請於命令列終端機上輸入以下的指令：

```
docker run --help
 ```

### 四、在網頁使用者介面上開啟服務

Bitmark節點包含了一個用於檢視及控制的網頁使用者介面。執行了第三步驟並且運行了Bitmark節點之後，您可以開啟網頁使用者介面來啟動`bitmarkd`及`recorderd`選項程式。

在多數的電腦系統中，網頁使用者介面可以用`localhost`位址(`127.0.0.1`)上的`9980`連接埠來存取，如下面的鏈結：

> [http://127.0.0.1:9980](http://127.0.0.1:9980)

載入網頁使用者介面之後，您可以在上面啟動兩個主要的 Bitmark 節點程式：

1. `bitmarkd` - 負責驗證 Bitmark 交易並記錄於 Bitmark 區塊鏈上（所有 Bitmark 節點都必須執行此程式）
2. `recorderd` - 負責運算 Bitmark 區塊鏈的工作量證明演算法，該演算法決定一個節點是否贏得某區塊並獲得獎金（此為選項程式）

第一次開始執行`bitmarkd`之後，節點會經過一個`Resynchronizing`的同步階段。此階段會下載目前 Bitmark 區塊鏈上的資訊至您的節點。一旦同步階段完成之後，您的 Bitmark 節點會開始為最新的區塊做驗證並且記錄交易。


## 設定選項

### 目前的區塊鏈

Bitmark 節點有兩種 Bitmark 區塊鏈讓參與者選擇：

- `bitmark` - 正式的 Bitmark 區塊鏈
- `testing` - 一個專門給開發用的`testnet`版本區塊鏈

參與節點的使用者可以在網頁使用者介面上面選擇其中一種來作為目前的區塊鏈。要注意的是轉換至不同的鏈時會需要在網頁使用者介面上重啟新鏈的`bitmarkd`及`recorderd`程式。

無論是`bitmark`或`testing`區塊鏈，Bitmark 系統都會給予贏得區塊的人獎金。

## 付款地址

Bitmark 節點的參與者在`bitmark`或`testing`上運行`bitmarkd`及`recorderd`並且贏得區塊之後，會得到獎金作為獎勵。獎金會（依照當時的加密貨幣價格及確認時間）以 bitcoin 或 litecoin 的形式支付至指定的 bitcoin 或 litecoin 付款位址。

當第一次執行 Bitmark 節點軟體時，安裝程式會自動產生一組預設的 bitcoin 及 litecoin 付款地址。這些地址可以從 Bitmark 節點網頁使用者介面上檢視及設定。


### Docker執行命令選項

運行 Bitmark 節點時，在命令列終端機中使用 Docker `run` 指令可以做許多不同的環境設定，如連接埠及 IP 位址：

```
docker run -d --name bitmarkNode -p 9980:9980 \
-p 2136:2136 -p 2130:2130 \
-e PUBLIC_IP=[YOUR_PUBLIC_IP] \
-v $HOME/bitmark-node-data/db:/.config/bitmark-node/db \
-v $HOME/bitmark-node-data/data:/.config/bitmark-node/bitmarkd/bitmark/data \
-v $HOME/bitmark-node-data/data-test:/.config/bitmark-node/bitmarkd/testing/data \
bitmark/bitmark-node
```

下表列出了許多`run`指令可執行的設定選項：

| 選項  | 預設值  | 說明  |
|:---|:---|:---|
| `-name`  | `bitmarkNode` | 為 Bitmark 節點所在的 Docker container 命名 |
| `-p`  | `9980` | 網頁使用者介面的網頁伺服器連接埠 |
| `-p`  | `2136` | 連接至其他節點的 bitmarkd 的連接埠 |
| `-p`  | `2135` | 連接至其他節點的 bitmarkd 的連接埠 |
| `-p`  | `2130` | Bitmark 節點 [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) 伺服器的連接埠 |
| `-e`  | `PUBLIC_IP=[YOUR_PUBLIC_IP]` | 註冊節點公有 IP 位址的環境參數 |

### Docker Compose 設定

熟悉 [Docker Compose](https://docs.docker.com/compose/) 的參與者可以使用內附的 `docker-compose.yml` 檔案做為設定 Bitmark 節點服務的範例。

可設定的選項有：

  - 環境：
    - PUBLIC_IP: 您的公開 IP 位址
  - 連接埠:
    - 2130: RPC 伺服器連接埠
    - 2135 & 2136: Peering 連接埠
    - 9980: 網頁伺服器連接埠
    _(提示：請確認使用 TCP 設定您的網路的 port forwarding 以確保公共網路可以存取您的節點)_
  - Volumes:
    - /.config/bitmark-node/bitmarkd/bitmark/data - 用於儲存`bitmark`的資料
    - /.config/bitmark-node/bitmarkd/testing/data - 用於儲存`testing`的資料


## 更新

**欲更新 Bitmark 節點軟體，請完成以下三個步驟：**

### ㄧ、下載最新版本的節點

欲更新 Bitmark 節點軟體至最新版本，開啟命令列終端機或命令提示字元，例如在 Mac 上的 Terminal 或是在 Windows 上的`cmd.exe`。然後輸入以下的指令來下載 Bitmark 節點軟體更新：

```
docker pull bitmark/bitmark-node
```

輸入 pull 指令之後，下載應該就會開始執行。成功下載完成後，您會收到以下訊息：

```
Status: Downloaded newer image for bitmark/bitmark-node:latest
```


### 二、執行 Bitmark 節點

成功下載軟體更新之後，請在命令列終端機利用下列指令，移除舊版節點並重新運行節點：

```
docker rm -f bitmarkNode
docker run -d --name bitmarkNode -p 9980:9980 \
-p 2136:2136 -p 2130:2130 \
-e PUBLIC_IP=[YOUR_PUBLIC_IP] \
-v $HOME/bitmark-node-data/db:/.config/bitmark-node/db \
-v $HOME/bitmark-node-data/data:/.config/bitmark-node/bitmarkd/bitmark/data \
-v $HOME/bitmark-node-data/data-test:/.config/bitmark-node/bitmarkd/testing/data \
bitmark/bitmark-node
```


### 三、在網頁使用者介面重新啟動服務

最後，在網頁使用者介面上重啟`bitmarkd`及選擇性重啟`recorderd`程式。在多數的電腦系統中，網頁使用者介面可以用`localhost`位址(`127.0.0.1`)上的`9980`連接埠來存取，如下面的鏈結：

> [http://127.0.0.1:9980](http://127.0.0.1:9980)

載入網頁使用者介面之後，您可以在上面啟動兩個主要的 Bitmark 節點程式：

1. `bitmarkd` - 負責驗證 Bitmark 交易並記錄於 Bitmark 區塊鏈上（所有 Bitmark 節點都必須執行此程式）
2. `recorderd` - 負責運算 Bitmark 區塊鏈的工作量證明演算法，該演算法決定一個節點是否贏得某區塊並獲得獎金（此為選項程式）

重新執行`bitmarkd`之後，節點會經過一個`Resynchronizing`的同步階段。此階段會下載目前 Bitmark 區塊鏈上的資訊至您的節點。一旦同步階段完成之後，您的 Bitmark 節點會開始為最新的區塊做驗證並且記錄交易。
