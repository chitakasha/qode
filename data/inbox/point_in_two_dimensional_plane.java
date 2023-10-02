public class Point {
  // Instance variables for x and y coordinates
  private double x;
  private double y;

  // Constructor that takes x and y as parameters
  public Point(double x, double y) {
    this.x = x;
    this.y = y;
  }

  // Getter methods for x and y
  public double getX() {
    return x;
  }

  public double getY() {
    return y;
  }

  // A method that calculates the distance between this point and another point
  public double distance(Point other) {
    // Use the Pythagorean theorem to calculate the distance
    double dx = this.x - other.x;
    double dy = this.y - other.y;
    return Math.sqrt(dx * dx + dy * dy);
  }
}

