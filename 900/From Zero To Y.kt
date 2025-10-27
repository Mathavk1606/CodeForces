fun main() {
    val t = readLine()!!.toInt()
    repeat(t) {
        val result = solve()
        println(result)
    }
}

fun solve(): Int {
    val (x, y) = readLine()!!.split(" ").map { it.toInt() }
    
    val possible = mutableListOf(1, x)
    
    var n = 10
    while (n < y) {
        possible.add(x * n)
        n *= 10
    }
    
    var operations = 0
    var currentY = y
    
    for (i in possible.size - 1 downTo 0) {
        if (currentY % possible[i] == 0) {
            operations += currentY / possible[i]
            break
        } else {
            val possibleRemovals = currentY / possible[i]
            operations += possibleRemovals
            currentY -= possibleRemovals * possible[i]
        }
    }
    
    return operations
}