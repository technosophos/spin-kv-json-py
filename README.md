# JSON and KV Store inside of Spin with Python

This is an example of using Spin's built-in [KV Store](https://developer.fermyon.com/spin/v2/key-value-store-tutorial) to store and retrieve JSON documents in Python.

It exemplifies a similar pattern to the built-in JSON handling in the Spin SDK for JS/TS.

## Prerequisites

* [Spin](https://developer.fermyon.com/spin)

## Installing

* Build with `spin build`

```
$ spin build
```

## Running

Use `spin build --up` to run locally, or `spin build && spin deploy` to deploy to Fermyon Cloud.

Once you have a server running, you can test with Curl or a web browser:

```console
$ curl localhost:3000
Hello visitor 1
$ curl localhost:3000
Hello visitor 2
$ curl localhost:3000
Hello visitor 3
```
