
#include "comm.h"

void chidprocess(int confd);

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
        chdpid = fork();
        if (0 == chdpid)
        {
        	close(lstfd);
        	chidprocess(confd);
        	exit(0);
        }
        close(confd);
    }



	return 0;
}

void chidprocess(int confd)
{
	ssize_t  n = 0;
	const int MAX_READLEN = 1024;
	char buf[MAX_READLEN];

	std::cout << "Entering chidprocess(). client fd = " << confd << std::endl;
    while(1)
    {
    	memset(buf, sizeof(buf), 0);
        n = recv(confd, (void *)&buf, sizeof(buf), 0);
        if(-1 == n)
        {
			std::cerr << "error!!! recv msg from client failed! nret = " << n << std::endl;
			exit(1);
        }
        std::cout << "recv msg from client succed! msg len = " << n << std::endl;
    }
}


