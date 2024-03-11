/******************************************************************************
 *
 * File:            PdfTools_PdfTools.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLS_H__
#define PDFTOOLS_PDFTOOLS_H__

#ifndef PDFTOOLS_CALL
#if defined(WIN32)
#define PDFTOOLS_CALL __stdcall
#else
#define PDFTOOLS_CALL
#endif
#endif

#include "PdfTools_Types.h"
#include "PdfTools_PdfToolsSys.h"

#ifdef __cplusplus
extern "C"
{
#endif

#ifdef _UNICODE
#define PdfTools_GetLastErrorMessage PdfTools_GetLastErrorMessageW
#define PdfTools_Sdk_Initialize      PdfTools_Sdk_InitializeW

#define PdfTools_Sdk_GetVersion PdfTools_Sdk_GetVersionW

#define PdfTools_Sdk_GetProducerFullName PdfTools_Sdk_GetProducerFullNameW

#define PdfTools_Sdk_GetProxy            PdfTools_Sdk_GetProxyW
#define PdfTools_Sdk_SetProxy            PdfTools_Sdk_SetProxyW
#define PdfTools_Sdk_GetLicensingService PdfTools_Sdk_GetLicensingServiceW
#define PdfTools_Sdk_SetLicensingService PdfTools_Sdk_SetLicensingServiceW

#define PdfTools_StringList_Get PdfTools_StringList_GetW
#define PdfTools_StringList_Add PdfTools_StringList_AddW

#define PdfTools_MetadataDictionary_Get      PdfTools_MetadataDictionary_GetW
#define PdfTools_MetadataDictionary_GetKey   PdfTools_MetadataDictionary_GetKeyW
#define PdfTools_MetadataDictionary_GetValue PdfTools_MetadataDictionary_GetValueW
#define PdfTools_MetadataDictionary_Set      PdfTools_MetadataDictionary_SetW
#define PdfTools_MetadataDictionary_SetValue PdfTools_MetadataDictionary_SetValueW

#define PdfTools_HttpClientHandler_SetClientCertificate       PdfTools_HttpClientHandler_SetClientCertificateW
#define PdfTools_HttpClientHandler_SetClientCertificateAndKey PdfTools_HttpClientHandler_SetClientCertificateAndKeyW

#else
#define PdfTools_GetLastErrorMessage PdfTools_GetLastErrorMessageA
#define PdfTools_Sdk_Initialize      PdfTools_Sdk_InitializeA

#define PdfTools_Sdk_GetVersion PdfTools_Sdk_GetVersionA

#define PdfTools_Sdk_GetProducerFullName PdfTools_Sdk_GetProducerFullNameA

#define PdfTools_Sdk_GetProxy            PdfTools_Sdk_GetProxyA
#define PdfTools_Sdk_SetProxy            PdfTools_Sdk_SetProxyA
#define PdfTools_Sdk_GetLicensingService PdfTools_Sdk_GetLicensingServiceA
#define PdfTools_Sdk_SetLicensingService PdfTools_Sdk_SetLicensingServiceA

#define PdfTools_StringList_Get PdfTools_StringList_GetA
#define PdfTools_StringList_Add PdfTools_StringList_AddA

#define PdfTools_MetadataDictionary_Get      PdfTools_MetadataDictionary_GetA
#define PdfTools_MetadataDictionary_GetKey   PdfTools_MetadataDictionary_GetKeyA
#define PdfTools_MetadataDictionary_GetValue PdfTools_MetadataDictionary_GetValueA
#define PdfTools_MetadataDictionary_Set      PdfTools_MetadataDictionary_SetA
#define PdfTools_MetadataDictionary_SetValue PdfTools_MetadataDictionary_SetValueA

#define PdfTools_HttpClientHandler_SetClientCertificate       PdfTools_HttpClientHandler_SetClientCertificateA
#define PdfTools_HttpClientHandler_SetClientCertificateAndKey PdfTools_HttpClientHandler_SetClientCertificateAndKeyA

#endif

/******************************************************************************
 * Library
 *****************************************************************************/
PDFTOOLS_EXPORT void PDFTOOLS_CALL PdfTools_Initialize();
PDFTOOLS_EXPORT void PDFTOOLS_CALL PdfTools_Uninitialize();

PDFTOOLS_EXPORT TPdfTools_ErrorCode PDFTOOLS_CALL PdfTools_GetLastError();
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL              PdfTools_GetLastErrorMessageA(char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL              PdfTools_GetLastErrorMessageW(WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT void PDFTOOLS_CALL PdfTools_SetLastErrorA(TPdfTools_ErrorCode iErrorCode, const char* szErrorMessage);
PDFTOOLS_EXPORT void PDFTOOLS_CALL PdfTools_SetLastErrorW(TPdfTools_ErrorCode iErrorCode, const WCHAR* szErrorMessage);

/******************************************************************************
 * Object
 *****************************************************************************/
PDFTOOLS_EXPORT void PDFTOOLS_CALL PdfTools_Release(void* pObject);
PDFTOOLS_EXPORT void PDFTOOLS_CALL PdfTools_AddRef(void* pObject);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_Equals(void* pObject, void* pOther);
PDFTOOLS_EXPORT int PDFTOOLS_CALL  PdfTools_GetHashCode(void* pObject);
/******************************************************************************
 * ConsumptionData
 *****************************************************************************/
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfTools_ConsumptionData_GetRemainingPages(TPdfTools_ConsumptionData* pConsumptionData);
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfTools_ConsumptionData_GetOverconsumption(TPdfTools_ConsumptionData* pConsumptionData);

/******************************************************************************
 * LicenseInfo
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_LicenseInfo_IsValid(TPdfTools_LicenseInfo* pLicenseInfo);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_LicenseInfo_GetExpirationDate(TPdfTools_LicenseInfo* pLicenseInfo,
                                                                          TPdfToolsSys_Date*     pExpirationDate);
PDFTOOLS_EXPORT TPdfTools_ConsumptionData* PDFTOOLS_CALL
PdfTools_LicenseInfo_GetConsumptionData(TPdfTools_LicenseInfo* pLicenseInfo);

/******************************************************************************
 * Sdk
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_Sdk_InitializeA(const char* szLicense, const char* szProducerSuffix);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_Sdk_InitializeW(const WCHAR* szLicense, const WCHAR* szProducerSuffix);

PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_Sdk_GetVersionA(char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_Sdk_GetVersionW(WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_Sdk_GetProducerFullNameA(char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_Sdk_GetProducerFullNameW(WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_Sdk_GetProxyA(char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_Sdk_GetProxyW(WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfTools_Sdk_SetProxyA(const char* szProxy);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfTools_Sdk_SetProxyW(const WCHAR* szProxy);
PDFTOOLS_EXPORT TPdfTools_HttpClientHandler* PDFTOOLS_CALL PdfTools_Sdk_GetHttpClientHandler(void);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL                         PdfTools_Sdk_GetUsageTracking(void);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL                         PdfTools_Sdk_SetUsageTracking(BOOL bUsageTracking);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_Sdk_GetLicensingServiceA(char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_Sdk_GetLicensingServiceW(WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfTools_Sdk_SetLicensingServiceA(const char* szLicensingService);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfTools_Sdk_SetLicensingServiceW(const WCHAR* szLicensingService);
PDFTOOLS_EXPORT TPdfTools_LicenseInfo* PDFTOOLS_CALL PdfTools_Sdk_GetLicenseInfoSnapshot(void);

/******************************************************************************
 * StringList
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfTools_StringList* PDFTOOLS_CALL PdfTools_StringList_New(void);

PDFTOOLS_EXPORT int PDFTOOLS_CALL    PdfTools_StringList_GetCount(TPdfTools_StringList* pStringList);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_StringList_GetA(TPdfTools_StringList* pStringList, int iIndex,
                                                              char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_StringList_GetW(TPdfTools_StringList* pStringList, int iIndex,
                                                              WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfTools_StringList_AddA(TPdfTools_StringList* pStringList, const char* szString);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfTools_StringList_AddW(TPdfTools_StringList* pStringList, const WCHAR* szString);

/******************************************************************************
 * MetadataDictionary
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfTools_MetadataDictionary* PDFTOOLS_CALL PdfTools_MetadataDictionary_New(void);

PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfTools_MetadataDictionary_GetCount(TPdfTools_MetadataDictionary* pMetadataDictionary);
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfTools_MetadataDictionary_GetSize(TPdfTools_MetadataDictionary* pMetadataDictionary); // Deprecated in Version 2.11.0.
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfTools_MetadataDictionary_GetBegin(TPdfTools_MetadataDictionary* pMetadataDictionary);
PDFTOOLS_EXPORT int PDFTOOLS_CALL PdfTools_MetadataDictionary_GetEnd(TPdfTools_MetadataDictionary* pMetadataDictionary);
PDFTOOLS_EXPORT int PDFTOOLS_CALL PdfTools_MetadataDictionary_GetNext(TPdfTools_MetadataDictionary* pMetadataDictionary,
                                                                      int                           it);
PDFTOOLS_EXPORT int PDFTOOLS_CALL PdfTools_MetadataDictionary_GetA(TPdfTools_MetadataDictionary* pMetadataDictionary,
                                                                   const char*                   szKey);
PDFTOOLS_EXPORT int PDFTOOLS_CALL PdfTools_MetadataDictionary_GetW(TPdfTools_MetadataDictionary* pMetadataDictionary,
                                                                   const WCHAR*                  szKey);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_MetadataDictionary_GetKeyA(
    TPdfTools_MetadataDictionary* pMetadataDictionary, int it, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_MetadataDictionary_GetKeyW(
    TPdfTools_MetadataDictionary* pMetadataDictionary, int it, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_MetadataDictionary_GetValueA(
    TPdfTools_MetadataDictionary* pMetadataDictionary, int it, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfTools_MetadataDictionary_GetValueW(
    TPdfTools_MetadataDictionary* pMetadataDictionary, int it, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_MetadataDictionary_SetA(TPdfTools_MetadataDictionary* pMetadataDictionary,
                                                                    const char* szKey, const char* szValue);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_MetadataDictionary_SetW(TPdfTools_MetadataDictionary* pMetadataDictionary,
                                                                    const WCHAR* szKey, const WCHAR* szValue);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfTools_MetadataDictionary_SetValueA(TPdfTools_MetadataDictionary* pMetadataDictionary, int it, const char* szValue);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfTools_MetadataDictionary_SetValueW(TPdfTools_MetadataDictionary* pMetadataDictionary, int it, const WCHAR* szValue);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_MetadataDictionary_Clear(TPdfTools_MetadataDictionary* pMetadataDictionary);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_MetadataDictionary_Remove(TPdfTools_MetadataDictionary* pMetadataDictionary,
                                                                      int                           it);

/******************************************************************************
 * HttpClientHandler
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfTools_HttpClientHandler* PDFTOOLS_CALL PdfTools_HttpClientHandler_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfTools_HttpClientHandler_SetClientCertificateA(TPdfTools_HttpClientHandler*         pHttpClientHandler,
                                                 const TPdfToolsSys_StreamDescriptor* pArchive, const char* szPassword);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_HttpClientHandler_SetClientCertificateW(
    TPdfTools_HttpClientHandler* pHttpClientHandler, const TPdfToolsSys_StreamDescriptor* pArchive,
    const WCHAR* szPassword);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_HttpClientHandler_SetClientCertificateAndKeyA(
    TPdfTools_HttpClientHandler* pHttpClientHandler, const TPdfToolsSys_StreamDescriptor* pCert,
    const TPdfToolsSys_StreamDescriptor* pKey, const char* szPassword);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_HttpClientHandler_SetClientCertificateAndKeyW(
    TPdfTools_HttpClientHandler* pHttpClientHandler, const TPdfToolsSys_StreamDescriptor* pCert,
    const TPdfToolsSys_StreamDescriptor* pKey, const WCHAR* szPassword);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_HttpClientHandler_AddTrustedCertificate(
    TPdfTools_HttpClientHandler* pHttpClientHandler, const TPdfToolsSys_StreamDescriptor* pCert);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfTools_HttpClientHandler_GetSslVerifyServerCertificate(TPdfTools_HttpClientHandler* pHttpClientHandler);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfTools_HttpClientHandler_SetSslVerifyServerCertificate(
    TPdfTools_HttpClientHandler* pHttpClientHandler, BOOL bSslVerifyServerCertificate);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLS_H__ */
