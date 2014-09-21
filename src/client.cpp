
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

    SMsg msg;
    msg.nSKey = htonl(SKEY);
    msg.nMsgType = htonl(ETMSY_HELLO);
    msg.nMsgLen = htonl(sizeof(msg));
    msg.nData = htonl(789654);

	while (1)
	{
		ssize_t zret = 0;

		zret = send(fd, (void *) (&msg), sizeof(msg), 0);
		if (-1 == zret) {
			std::cerr << "error!!! send msg to server failed! nret = " << nret
					<< std::endl;
			exit(1);
		}
		std::cout << "send msg to server succed! zret = " << zret << std::endl;
		sleep(2);
	}
    close(fd);

	return 0;
}
