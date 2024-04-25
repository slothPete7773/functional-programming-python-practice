# Essential cores in Functional Programming

According to this [blog](https://medium.com/odds-team/functional-programming-in-python-part1-do-1-thing-and-do-it-well-f0722227057f) though.

1. function should do one thing and do it well
2. function as a first class citizen
3. higher-order function
4. unary function
5. currying
6. function composition
7. handle error in functional way using Monadic (Monad)

# Organization in this repository

This repository is a tutorial that follows guidance and approach that has been written in the article; [Functional Programming in Python](https://medium.com/odds-team/functional-programming-in-python-part1-do-1-thing-and-do-it-well-f0722227057f) by RuufimoN at ODDs.

Source code will be constructed with the ordering label, from first to last. Where each subsequent snippet will be the extended of the previous snippet to become more functional.

The goal is to make the procedural Python code to be as close as Scala functional code.

Here is the goal Scala snippet.

```scala
import cats.implicits._
import scala.io.Source
import scala.util.{Try, Success, Failure}

object Entry extends App {
  def readCsvFile(filePath: String): Try[List[List[String]]] =
    println(s"Reading file $filePath")
    Try(Source.fromFile(filePath).getLines().map(_.split(",").toList).toList)

  // Function to extract a column
  def extractColumn(columnIndex: Int, data: List[List[String]]): Try[List[Double]] =
    println(s"Extracting column $columnIndex")
    Try(data.tail.map(row => row(1).toDouble))

  // Function to calculate average
  def calculateAverage(columnValues: List[Double]): Try[Double] =
    println("Calculating average")
    if (columnValues.isEmpty) Failure(new IllegalArgumentException("Empty column"))
    else Success(columnValues.sum / columnValues.length)

  // Data pipeline
  val csvFilePath = "example.csv"

  val result: Try[Double] =
    readCsvFile(csvFilePath)
      .flatMap(data => extractColumn(1, data))
      .flatMap(calculateAverage)

  result match {
    case Success(avg) => println(s"The average is: $avg")
    case Failure(err) => println(s"Error processing data: ${err.getMessage}")
  }
}
```

# 1.1 Do one thing

The function `extract_column()` initially perform more than 1 responsibility. Therefore, it is broken down into ssmaller functions, each with its own responsible.

At first, removing header function is a function named `remove_header()` but it is too specific, not good for reusability. It got changed to `remove_header() -> remove_rows()` to make it more generic and convenience for modularity and reusability.

The same true for 

- `convert_to_float()` -> `convert_to()` : A float converter function is change to generic converter, instead of fixing the float parser in the function, we can provide any arbitrary converter as a function argument.
