#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include<string.h>

#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>


const int MAX_CLICONN = 100;
const unsigned short SVRPORT = 8888;

typedef  unsigned int UINT;
const UINT SKEY = 0xdeedbeef;
enum EMsgType
{
	ETMSY_HELLO = 1,
};
struct SMsg
{
	UINT nSKey;
	UINT nMsgType;
    UINT nMsgLen;
    UINT nData;
};
