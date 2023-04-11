package hello.servlet.basic.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Enumeration;

@WebServlet(name = "requestHeaderServlet", urlPatterns = "/request-header")
public class RequestHeaderServlet extends HttpServlet {
    protected void service(HttpServletRequest request, HttpServletResponse response ) throws ServletException{
        printStartLine(request);
        printHeaders(request);
    }

    protected void printStartLine(HttpServletRequest request) {
        System.out.println("---REQUEST-LINE - staet ---");

    }
    protected void printHeaders(HttpServletRequest request) {
        Enumeration<String> headerNames = request.getHeaderNames();
        while (headerNames.hasMoreElements()) {
            String headerName = headerNames.nextElement();
            System.out.println(headerName + ":" + headerName);
        }
    }
}
