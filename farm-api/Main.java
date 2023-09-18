//this is method2 for getting API data in java
//supposedly this one is better but only works on Java => 11
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

public class Main
{
	public static void main(String args[])
	{
		HttpClient client = HttpClient.newHttpClient();
		HttpRequest request = HttpRequest.newBuilder().uri(URI.create("https://api.openweathermap.org/data/2.5/weather?lat=47.10&lon=-123.05&appid=2509420cdb43a79b9f4fe083772cfe0c")).build();
		client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
			.thenApply(HttpResponse::body)
			.thenAccept(System.out::println)
			.join();
	}
}

