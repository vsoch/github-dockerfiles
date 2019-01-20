# Transactions

> NOTE: The specification documented below is still highly active in development
and subject to change.

## Routing

Ethermint needs to parse and handle transactions routed for both the EVM and for
the Cosmos hub. We attempt to achieve this by mimicking
[Geth's](https://github.com/ethereum/go-ethereum) `Transaction` structure and
treat it as a unique Cosmos SDK message type. An Ethereum transaction is a single
[`sdk.Msg`](https://godoc.org/github.com/cosmos/cosmos-sdk/types#Msg) contained
in an [`auth.StdTx`](https://godoc.org/github.com/cosmos/cosmos-sdk/x/auth#StdTx).
All relevant Ethereum transaction information is contained in this message. This
includes the signature, gas, payload, etc.

Being that Ethermint implements the Tendermint ABCI application interface, as
transactions are consumed, they are passed through a series of handlers. Once such
handler, the `AnteHandler`, is responsible for performing preliminary message
execution business logic such as fee payment, signature verification, etc. This is
particular to Cosmos SDK routed transactions. Ethereum routed transactions will
bypass this as the EVM handles the same business logic.

Ethereum routed transactions coming from a web3 source are expected to be RLP
encoded, however all internal interaction between Ethermint and Tendermint will
utilize Amino encoding.

__Note__: Our goal is to utilize Geth/Turbo-Geth as a library, at least as much
as possible, so it should be expected that these types and the operations you may
perform on them will keep in line with Ethereum (e.g. signature algorithms and
gas/fees). In addition, we aim to have existing tooling and frameworks in the
Ethereum ecosystem have 100% compatibility with creating transactions in Ethermint.

## Signatures

Ethermint supports [EIP-155](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md)
signatures. A `Transaction` is expected to have a single signature for Ethereum
routed transactions. However, just as in Cosmos, Ethermint will support multiple
signers for non-Ethereum transactions. Signatures over the
`Transaction` type are identical to Ethereum and the signatures will not be duplicated
in the embedding [`auth.StdTx`](https://godoc.org/github.com/cosmos/cosmos-sdk/x/auth#StdTx).

## Gas & Fees

TODO
# EVM

TODO
# Introduction

## What is Ethermint

Ethermint is a high throughput PoS blockchain that is fully compatible and
interoperable with Ethereum. In other words, it allows for running vanilla Ethereum
on top of [Tendermint](https://github.com/tendermint/tendermint) consensus via
the [Cosmos SDK](https://github.com/cosmos/cosmos-sdk/). This allows developers
to have all the desired features of Ethereum, while at the same time benefit
from Tendermint’s PoS implementation. Also, because it is built on top of the
Cosmos SDK, it will be able to exchange value with the rest of the Cosmos Ecosystem.

Here’s a glance at some of the key features of Ethermint:

* Web3 compatibility
* High throughput
* Horizontal scalability
* Transaction finality

Ethermint enables these key features through:

* Implementing Tendermint's ABCI application interface to manage the base Blockchain
* Leveraging [modules](https://github.com/cosmos/cosmos-sdk/tree/master/x/) and other mechanisms implemented by the Cosmos SDK
* Utilizing [`geth`](https://github.com/ethereum/go-ethereum) as a library to avoid code reuse and improve maintainability
* Exposing a fully compatible Web3 RPC layer for interacting with the system

The sum of these features allows developers to leverage existing Ethereum ecosystem
tooling and software to seamlessly deploy smart contracts which interact with the rest of the Cosmos
ecosystem!

## In-depth Topics

### Tendermint Core & the Application Blockchain Interface (ABCI)

Tendermint consists of two chief technical components: a blockchain consensus
engine and a generic application interface. The consensus engine, called
Tendermint Core, ensures that the same transactions are recorded on every machine
in the same order. The application interface, called the Application Blockchain
Interface (ABCI), enables the transactions to be processed in any programming
language.

Tendermint has evolved to be a general purpose blockchain consensus engine that
can host arbitrary application states. Since Tendermint can replicate arbitrary
applications, it can be used as a plug-and-play replacement for the consensus
engines of other blockchains. Ethermint is such an example of an ABCI application
replacing Ethereum's PoW via Tendermint's consensus engine.

Another example of a cryptocurrency application built on Tendermint is the Cosmos
network. Tendermint is able to decompose the blockchain design by offering a very
simple API (ie. the ABCI) between the application process and consensus process.
