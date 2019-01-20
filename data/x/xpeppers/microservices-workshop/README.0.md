## XPeppers Microservices Workshop
### A monolithic e-commerce application

#### How to build the application
Maven is needed.
From the project root folder:

`
mvn package
`

#### How to run the application

`
java -jar target/monolith-1.0-SNAPSHOT-jar-with-dependencies.jar
`

After the application is started, it will be available at the address:

`
http://localhost:4567
`

#### Usage examples
**Make a new order**

`
curl -X POST -d "product_code=111&product_quantity=1" localhost:4567/orders
`

Responses:
`order confirmed` or `product not available`

**Get all the orders**

`
curl localhost:4567/orders
`

Response:
```json
[
    {
        "id": "1c35b140-58f7-4cd9-8e4e-6e94d304e428",
        "productCode": "111",
        "productQuantity": 1
    }
]
```

#### Build Docker image

```
docker build -t commerce.monolith .
```

#### Run Docker container

```
docker run -it --rm --name monolith -p 4567:4567 commerce.monolith:latest
```## XPeppers Microservices Workshop
### The warehouse application

#### How to build the application
Maven is needed.
From the project root folder:

`
mvn package
`

#### How to run the application

`
java -jar target/warehouse-1.0-SNAPSHOT-jar-with-dependencies.jar
`

After the application is started, it will be available at the address:

`
http://localhost:8181
`

#### Usage examples
**Reserve products for an Order**

`
curl -X POST -d "product_code=111&product_quantity=1&order_id=3b3a2a7a-6d52-11e8-adc0-fa7ae01bbebc" http://localhost:8181/pickProducts
`

**Get all the reserved products**

`
curl localhost:8181/reservedProducts
`

Response:
```json
[
  {
    "orderId": "3b3a2a7a-6d52-11e8-adc0-fa7ae01bbebc",
    "code": "111",
    "quantity": 1
   }
]
```## XPeppers Microservices Workshop
### The orders application

#### How to build the application
Maven is needed.
From the project root folder:

`
mvn package
`

#### How to run the application

`
java -jar target/orders-1.0-SNAPSHOT-jar-with-dependencies.jar
`

After the application is started, it will be available at the address:

`
http://localhost:4567
`

#### Usage examples
**Make a new order**

`
curl -X POST -d "product_code=111&product_quantity=1" localhost:4567/orders
`

Responses:
`order confirmed` or `product not available`

**Get all the orders**

`
curl localhost:4567/orders
`

Response:
```json
[
    {
        "id": "1c35b140-58f7-4cd9-8e4e-6e94d304e428",
        "productCode": "111",
        "productQuantity": 1
    }
]
```## XPeppers Microservices Workshop
### The payments application

#### How to build the application
Maven is needed.
From the project root folder:

`
mvn package
`

#### How to run the application

`
java -jar target/payments-1.0-SNAPSHOT-jar-with-dependencies.jar
`

After the application is started, it will be available at the address:

`
http://localhost:8282
`

#### Usage examples
**Make a new payment**

`
curl -X POST -d "order_id=42265410-6d7c-11e8-adc0-fa7ae01bbebc" http://localhost:8282/payments
`

**Get all the payments**

`
curl localhost:8282/payments
`