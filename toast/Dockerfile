FROM frekele/ant:1.10.1-jdk8
COPY . /toast
WORKDIR "/toast"
RUN ant
EXPOSE 1234
WORKDIR "/toast/dist"
CMD ["java","-jar","toast.jar"]
