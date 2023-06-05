import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class RubikaLogin {
  public static void main(String[] args) {
    System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");
    WebDriver driver = new ChromeDriver();
    // Navigate to the Rubika login page
    driver.get("https://rubika.ir/login");
    WebElement emailInput = driver.findElement(By.name("email"));
    emailInput.sendKeys("your_email@example.com");
    WebElement passwordInput = driver.findElement(By.name("password"));
    passwordInput.sendKeys("your_password");
    WebElement loginButton = driver.findElement(By.tagName("button"));
    loginButton.click();
    WebElement loggedInUser = driver.findElement(By.className("user-name"));
    if (loggedInUser.getText().equals("Your Name")) {
      System.out.println("Logged in successfully!");
    } else {
      System.out.println("Login failed!");
    }
    driver.quit();
  }
}
