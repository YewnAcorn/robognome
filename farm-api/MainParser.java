import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import org.json.JSONObject;
import org.json.JSONArray;

public class MainParser {
    
    public static void main(String[] args) throws IOException {
        
    	//creates new buffered reader to read WeatherReportJSON.txt
        BufferedReader br=new BufferedReader(new FileReader("/home/pi/Gardenbot/dsaGreenhouseProjectFall2022/testing-api/output.json"));            
        String line;  
        //create string builder object
        //loop through JSON file using the readLine method and
        //append to sbuilderObj
        StringBuilder sbuilderObj = new StringBuilder();
        while((line=br.readLine()) !=null){
            sbuilderObj.append(line);
        }
        //print out string builder contents
        //System.out.println("Original Json :: "+sbuilderObj.toString());
       
        //Using JSONObject 
        JSONObject jsonObj = new JSONObject(sbuilderObj.toString());
     
        JSONArray weather = jsonObj.getJSONArray("weather");
	JSONObject id = weather.getJSONObject(0);
	int weatherID = id.getInt("id");
        System.out.println(weatherID);
	//TODO add write to logs
	//
        
        /*
        //Using JSONArray
        JSONArray arrObj = jsonObj.getJSONArray("main");
        
        double temp = arrObj.getJSONObject(0).getDouble("temp");
        System.out.println(temp);
        */
        
        /*
        String name = jsonObj.getJSONObject("empInfo").getString("name");
        String position = jsonObj.getJSONObject("empInfo").getString("position");
        String age = jsonObj.getJSONObject("empInfo").getString("age");
        System.out.println("###### Emp Info ############");
        System.out.println("Name     : "+name);
        System.out.println("Position : "+position);
        System.out.println("Age      : "+age);
        
        //Fetching nested Json using JSONArray
        JSONArray arrObj = jsonObj.getJSONArray("skills");
        for (int i = 0; i < arrObj .length(); i++) {
        
            String programming = arrObj .getJSONObject(i).getString("programming");
            
            String scripting = arrObj .getJSONObject(i).getString("scripting");
            String ml = arrObj .getJSONObject(i).getString("ml");
          
            System.out.println("###### Emp Skills (nested) ###########");
            System.out.println("Programming : "+programming);
            System.out.println("Scripting   : "+scripting);
            System.out.println("Ml          : "+ml);
        }
        */
    }
}
