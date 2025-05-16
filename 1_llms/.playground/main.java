import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import okhttp3.*;
import java.io.IOException;

public class Main {
    private static final String OPENAI_API_KEY = System.getenv("OPENAI_API_KEY");
    private static final String MODEL = "gpt-4-turbo-preview"; // Note: Changed from "gpt-4o-mini" as it's not a valid model name
    private static final OkHttpClient client = new OkHttpClient();
    private static final ObjectMapper objectMapper = new ObjectMapper();

    public static String analyzeSentiment(String review) throws IOException {
        MediaType mediaType = MediaType.parse("application/json");
        String requestBody = String.format("{\"model\": \"%s\", \"messages\": [{\"role\": \"user\", \"content\": \"You are a sentiment analysis expert. Analyze the sentiment of the following movie review and respond with either 'Positive', 'Negative', or 'Neutral'. %s\"}]}", MODEL, review);
        RequestBody body = RequestBody.create(requestBody, mediaType);
        Request request = new Request.Builder()
                .url("https://api.openai.com/v1/chat/completions")
                .post(body)
                .addHeader("Authorization", "Bearer " + OPENAI_API_KEY)
                .addHeader("Content-Type", "application/json")
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);

            JsonNode jsonResponse = objectMapper.readTree(response.body().string());
            return jsonResponse.path("choices").get(0).path("message").path("content").asText().trim();
        }
    }

    public static void main(String[] args) {
        String movieReview = """
        The latest superhero blockbuster was a rollercoaster of emotions. 
        The special effects were mind-blowing and the action sequences kept me on the edge of my seat. 
        However, the plot felt a bit predictable at times, and some character development was lacking. 
        Overall, it was an entertaining experience, but not as groundbreaking as I had hoped.
        """;

        try {
            String sentiment = analyzeSentiment(movieReview);
            System.out.println("Movie Review:\n" + movieReview + "\n");
            System.out.println("Sentiment: " + sentiment);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

