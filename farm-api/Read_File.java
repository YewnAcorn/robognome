import java.io.*;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Read_File {    
  List<String> Read_File(){
  // Initializing file Path with some conditions
  Path inputFilePath = Paths.get(".", "raincode.txt");
  Charset charset = StandardCharsets.UTF_8;
  
  // Create array of Strings for storing the data we read in
  List<String> lines;
  
    // Try to read in the lines
    try {
      // read content from file
      lines = Files.readAllLines(inputFilePath, charset);
      for(String line: lines) {
        System.out.println(line);
      }
    }

    // Catch possible errors so it doesn't crash the program
    // Might want to decide to take further action here
//* // Maybe want to write the exception to the file?
    catch (IOException e) {
      // Failsafe in case writing to file fails
      System.out.println("Exception caught.");
      e.printStackTrace();
    }
  }
}
