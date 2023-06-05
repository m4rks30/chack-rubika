import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
public class RubikaLogin {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        // Create a new instance of the ChromeDriver
        WebDriver driver = new ChromeDriver();
        driver.get("https://rubika.ir/login");
        WebElement usernameField = driver.findElement(By.name("username"));
        WebElement passwordField = driver.findElement(By.name("password"));
        usernameField.sendKeys("your_username");
        passwordField.sendKeys("your_password");
        WebElement loginButton = driver.findElement(By.cssSelector("button.btn-primary"));
        loginButton.click();
        WebElement userDashboard = driver.findElement(By.cssSelector("div#user-dashboard"));
        while (!userDashboard.isDisplayed()) {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        // ...
        driver.quit();
    }
}
