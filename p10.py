jdk 21
tomcat 9
Developing and Deploying Web Service in Java (SOAP using Maven & Tomcat)
#✅ STEP 1: Install Required Software
    Install JDK 8 adoptium: windows msi
    -> next
    -> next->install for all users
    -> 3rd option pe: will be installed on local harddrive
    Install Apache NetBeans 14
    Download and extract Apache Tomcat 9
    Example path:
    C:\apache-tomcat-9.0.xx

#✅ STEP 2: Configure Tomcat in NetBeans
    Open NetBeans
    Go to:
    Tools → Servers
    Click Add Server
    Select:
    Apache Tomcat or TomEE
    Browse and select Tomcat folder
    Click Finish

#👉 Tomcat will appear in:
    Services → Servers

#✅ STEP 3: Create Maven Web Application
    Click: File → New Project
    Select:
    Java with Maven → Web Application
    Click Next
    Enter:
    Project Name: prac10
    Group ID: com.mycompany
    Click Next
    Select:
    Server → Apache Tomcat 9
    (default rakho)
    Java EE Version → Java EE 7 Web
    Click Finish

#✅ STEP 4: Configure pom.xml
    Open pom.xml
    Ensure:
    <packaging>war</packaging>
    #Add dependency inside <dependencies>:
        
    <dependency>
        <groupId>com.sun.xml.ws</groupId>
        <artifactId>jaxws-rt</artifactId>
        <version>2.3.3</version>
    </dependency>
    
    #Add build plugin before </project>:
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.2.2</version>
            </plugin>
        </plugins>
    </build>
    Save file
    Right click project → Clean and Build
    
#✅ STEP 5: Create Web Service Class
    Go to Source Packages
    Right click → New → Java Package
    Name: com.mycompany.prac10
    Right click package → New → Java Class
    Name: HelloService
    Replace code:
package com.mycompany.prac10;

import javax.jws.WebService;
import javax.jws.WebMethod;

@WebService
public class HelloService {

    @WebMethod
    public String sayHello(String name) {
        return "Hello " + name;
    }
}
Save file
#run and build
#run project
#authentication ayega (incase dalna pade toh dalna)

#go tweb pages-> web inf-> web xml-> code auto generated->servlet name ko copy->browser wale link pe paste karo
#wsdl ka link daalo soap pe
incase inf nahi hoga then do this or else directly go to testing of SOAP

#✅ STEP 6: Create WEB-INF Folder
    Right click Web Pages
    Click New → Folder
    Name it: WEB-INF

#✅ STEP 7: Create web.xml
    Right click WEB-INF → New → XML Document
    Name: web
    Paste:
        
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         version="3.1">

    <listener>
        <listener-class>
            com.sun.xml.ws.transport.http.servlet.WSServletContextListener
        </listener-class>
    </listener>

    <servlet>
        <servlet-name>HelloService</servlet-name>
        <servlet-class>
            com.sun.xml.ws.transport.http.servlet.WSServlet
        </servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>HelloService</servlet-name>
        <url-pattern>/HelloService</url-pattern>
    </servlet-mapping>

</web-app>
Save file

#✅ STEP 8: Create sun-jaxws.xml
    Right click WEB-INF → New → XML Document
    Name: sun-jaxws
    Paste:
<?xml version="1.0" encoding="UTF-8"?>
<endpoints
    xmlns="http://java.sun.com/xml/ns/jax-ws/ri/runtime"
    version="2.0">

    <endpoint
        name="HelloService"
        implementation="com.mycompany.prac10.HelloService"
        url-pattern="/HelloService"/>
</endpoints>
Save file

#✅ STEP 9: Run the Project
Right click project → Run
Wait until deployment is successful

#✅ STEP 10: Check WSDL
Open browser
Enter:
http://localhost:8080/prac10/HelloService?wsdl

👉 If working, you will see XML starting with:
<definitions>

#=>Expected Output
WAR file created
Application deployed on Tomcat
WSDL file generated
Web Service accessible in browser

#Testing using SOAP UI
✅ Steps:
    Open SOAP UI
    Click:
    File → New SOAP Project
    Enter:
    Project Name: HelloServiceTest
    WSDL:
    http://localhost:8080/prac10/HelloService?wsdl
    ✔ Tick: Create Requests → Click OK

    Navigate:
    HelloServiceTest
     → HelloServiceSoapBinding
     → sayHello
     → Request 1
    Open Request 1
    Replace:
    <arg0>?</arg0>

With:

<arg0>Ashlesha</arg0>
Click Submit (▶)
Output:
<return>Hello Ashlesha</return>
✅ Final Result

👉 SOAP Web Service is successfully created, deployed, and tested.

===============================================================================================================
#####🔹 Q1. Implement and Consume a Hello World Service in Java

#✅ STEP 1: Install Required Software
Install JDK 8 (optional but recommended)
Install Apache NetBeans 14
Download and extract Apache Tomcat 9
#✅ STEP 2: Configure Tomcat in NetBeans
Open NetBeans
Go to: Tools → Servers
Click Add Server
Select Apache Tomcat
Browse Tomcat folder → Finish

👉 Appears in: Services → Servers

#✅ STEP 3: Create Maven Web Application
File → New Project
Java with Maven → Web Application
Project Name: HelloServiceApp
Group ID: com.mycompany
Select Server → Apache Tomcat 9
Java EE Version → Java EE 7 Web
Click Finish
#✅ STEP 4: Configure pom.xml

Add:

<packaging>war</packaging>

<dependency>
    <groupId>com.sun.xml.ws</groupId>
    <artifactId>jaxws-rt</artifactId>
    <version>2.3.3</version>
</dependency>

<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-war-plugin</artifactId>
            <version>3.3.2</version>
        </plugin>
    </plugins>
</build>

👉 Clean and Build

#✅ STEP 5: Create Web Service Class
package com.mycompany.helloservice;

import javax.jws.WebService;
import javax.jws.WebMethod;

@WebService
public class HelloService {

    @WebMethod
    public String greet(String name) {
        return "Hello " + name;
    }
}
#✅ STEP 6: Create WEB-INF Folder
Web Pages → New Folder → WEB-INF
#✅ STEP 7: Create web.xml
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" version="3.1">

    <listener>
        <listener-class>
            com.sun.xml.ws.transport.http.servlet.WSServletContextListener
        </listener-class>
    </listener>

    <servlet>
        <servlet-name>HelloService</servlet-name>
        <servlet-class>
            com.sun.xml.ws.transport.http.servlet.WSServlet
        </servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>HelloService</servlet-name>
        <url-pattern>/HelloService</url-pattern>
    </servlet-mapping>

</web-app>
#✅ STEP 8: Create sun-jaxws.xml
<endpoints xmlns="http://java.sun.com/xml/ns/jax-ws/ri/runtime" version="2.0">

    <endpoint
        name="HelloService"
        implementation="com.mycompany.helloservice.HelloService"
        url-pattern="/HelloService"/>
</endpoints>
#✅ STEP 9: Run the Project
Right click → Run
#✅ STEP 10: Check WSDL
http://localhost:8080/HelloServiceApp/HelloService?wsdl
#👉 Output
<return>Hello Riddhi</return>

==========================================================================================

###########🔹Q2. Implement and Consume Square and Cube Service in Java
#✅ STEP 1 to STEP 4

👉 SAME AS ABOVE (don’t rewrite in exam — mention “same as previous”)

#✅ STEP 5: Create Web Service Class
package com.mycompany.mathservice;

import javax.jws.WebService;
import javax.jws.WebMethod;

@WebService
public class MathService {

    @WebMethod
    public int square(int num) {
        return num * num;
    }

    @WebMethod
    public int cube(int num) {
        return num * num * num;
    }
}
#✅ STEP 6: Create WEB-INF Folder

(Same)

#✅ STEP 7: Create web.xml
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" version="3.1">

    <listener>
        <listener-class>
            com.sun.xml.ws.transport.http.servlet.WSServletContextListener
        </listener-class>
    </listener>

    <servlet>
        <servlet-name>MathService</servlet-name>
        <servlet-class>
            com.sun.xml.ws.transport.http.servlet.WSServlet
        </servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>MathService</servlet-name>
        <url-pattern>/MathService</url-pattern>
    </servlet-mapping>

</web-app>
#✅ STEP 8: Create sun-jaxws.xml
<endpoints xmlns="http://java.sun.com/xml/ns/jax-ws/ri/runtime" version="2.0">

    <endpoint
        name="MathService"
        implementation="com.mycompany.mathservice.MathService"
        url-pattern="/MathService"/>
</endpoints>
#✅ STEP 9: Run Project
#✅ STEP 10: Check WSDL
http://localhost:8080/prac10/MathService?wsdl
#👉 Output
<square>25</square>
<cube>125</cube>












For Viva - 

# Practical Viva Questions  
## Java SOAP Web Service (Maven + Tomcat + JAX-WS)  

---

## 1. Web Service Concepts  

**Q1. What is a Web Service?**  
A web service is a software system that allows communication between applications over a network.  

**Q2. What is SOAP Web Service?**  
SOAP (Simple Object Access Protocol) is a protocol used for exchanging structured information using XML.  

**Q3. What is WSDL?**  
WSDL (Web Services Description Language) is an XML document that describes the web service, its methods, and how to access it.  

---

## 2. Java Web Service Concepts  

**Q1. What is JAX-WS?**  
JAX-WS (Java API for XML Web Services) is a Java API used to create SOAP-based web services.  

**Q2. What is @WebService annotation?**  
It is used to define a class as a web service.  

**Q3. What is @WebMethod annotation?**  
It exposes a method so it can be accessed by clients.  

---

## 3. Maven Concepts  

**Q1. What is Maven?**  
Maven is a build automation and dependency management tool for Java projects.  

**Q2. What is pom.xml?**  
It is a configuration file that defines dependencies, plugins, and project settings.  

**Q3. What is dependency in Maven?**  
An external library required for the project.  

---

## 4. Tomcat Server  

**Q1. What is Apache Tomcat?**  
Apache Tomcat is a web server used to deploy and run Java web applications.  

**Q2. What is deployment?**  
The process of making a web application available on a server.  

**Q3. What is WAR file?**  
A Web Application Archive file used to deploy Java web applications.  

---

## 5. SOAP and XML Concepts  

**Q1. Why does SOAP use XML?**  
Because XML is platform-independent and structured.  

**Q2. What is SOAP message?**  
An XML-based message used to communicate between client and server.  

**Q3. What are parts of SOAP message?**  
Envelope, Header, Body  

---

## 6. Service Description and Access  

**Q1. What is the role of WSDL in SOAP?**  
It describes the service methods, parameters, and endpoint.  

**Q2. How does a client know how to call a SOAP service?**  
By reading the WSDL file.  

---

## 7. Client-Server Interaction  

**Q1. What is client-server architecture?**  
Client sends request → Server processes → Server sends response.  

**Q2. What is SOAP UI?**  
A tool used to test SOAP web services.  

**Q3. How does SOAP UI interact with service?**  
By sending XML requests based on WSDL.  

---

## 8. Application Logic Concepts  

**Q1. What is the purpose of Hello Service?**  
To return a greeting message.  

**Q2. What is the purpose of Math Service?**  
To perform operations like square and cube.  

**Q3. How are methods executed in web service?**  
Through remote calls via SOAP requests.  

---

## 9. Advantages and Limitations  

**Q1. Advantages of SOAP Web Services**  
Platform independent, secure, standardized  

**Q2. Limitations of SOAP**  
Heavy, slower due to XML, complex  

---

## 10. Comparison-Based Questions  

**Q1. Difference between SOAP and REST**  
SOAP → Protocol, XML, heavy  
REST → Architecture, JSON, lightweight  

**Q2. Difference between Web Service and Web Application**  
Web Service → Provides data  
Web App → Provides UI  

---

## 11. Final Conceptual Question  

**Q. Explain how this practical demonstrates web services.**  
In this practical, a Java-based SOAP web service is created using JAX-WS and deployed on Tomcat. The service methods are exposed via WSDL and tested using SOAP UI, demonstrating communication between client and server using XML-based messages.  

---
