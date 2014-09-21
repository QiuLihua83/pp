
#include "comm.h"

int main()
{
	int nret = 0;
    int fd = 0;
    struct sockaddr_in cliaddr;

    std::cout << "Client running......" <<  std::endl;
    fd = socket(AF_INET, SOCK_STREAM, 0);
    std::cout << "fd = " << fd << std::endl;

    bzero(&cliaddr, sizeof(cliaddr));
    cliaddr.sin_family = AF_INET;
    cliaddr.sin_port = htons(SVRPORT);

    nret = connect(fd, (struct sockaddr *)(&cliaddr), sizeof(cliaddr));
    if (0 != nret)
    {
    	std::cerr << "error!!! connect to server failed! nret = " << nret << std::endl;
        exit(1);
    }
    std::cout << "connect to server succed! nret = " << nret << std::endl;

    close(fd);

	return 0;
}
