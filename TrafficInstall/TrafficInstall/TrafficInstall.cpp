// TrafficInstall.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <tchar.h>
#include <urlmon.h>
#include "TrafficInstall.h"
#include <string> 
#include <iostream>
#pragma comment(lib, "urlmon.lib")

void print_LPTSTR(LPTSTR buf_to_print, uint64_t buf_len) {
	for (int i = 0; i < buf_len; i++)
	{
		std::wcout << buf_to_print[i];
	}
	printf("\r\n");
}

int list_all_env_vars() {
	LPTSTR lpszVariable;
	LPTCH lpvEnv;

	// Get a pointer to the environment block. 

	lpvEnv = GetEnvironmentStrings();

	// If the returned pointer is NULL, exit.
	if (lpvEnv == NULL)
	{
		printf("GetEnvironmentStrings failed (%d)\n", GetLastError());
		return 0;
	}

	// Variable strings are separated by NULL byte, and the block is 
	// terminated by a NULL byte. 

	lpszVariable = (LPTSTR)lpvEnv;

	while (*lpszVariable)
	{
		_tprintf(TEXT("%s\n"), lpszVariable);
		lpszVariable += lstrlen(lpszVariable) + 1;
	}
	FreeEnvironmentStrings(lpvEnv);
	return 1;
}

int main() {
	printf("Beginning Installation...\r\n");
	//HRESULT hr = URLDownloadToFile(NULL, _T("your web page"), _T("c:/web_page.html"), 0, NULL);
	//printf("HRESULT = %d", hr);
	LPTSTR PATH_ENV_BUF;
	PATH_ENV_BUF = (LPTSTR)malloc(4096*sizeof(TCHAR));
	GetEnvironmentVariable(PATH_VAR, PATH_ENV_BUF, 4096);
	print_LPTSTR(PATH_ENV_BUF, 4096);
	return 0;
}

