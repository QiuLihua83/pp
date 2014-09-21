
#include "comm.h"



int main()
{
	int lstfd = 0;
	int confd = 0;
	pid_t chdpid;
	socklen_t clilen;
	struct sockaddr_in cliaddr, servaddr;

	std::cout << "Server running......" <<  std::endl;
    lstfd = socket(AF_INET, SOCK_STREAM, 0);
    std::cout << "lstfd = " << lstfd << std::endl;

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(SVRPORT);

    bind(lstfd, (struct sockaddr *)(&servaddr), sizeof(servaddr));

    listen(lstfd, MAX_CLICONN);

    while(1)
    {
    	clilen = sizeof(cliaddr);
    	confd = accept(lstfd,(struct sockaddr *)&(cliaddr), &clilen);
        std::cout << "client fd = " << confd << std::endl;

    }



	return 0;
}
