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
