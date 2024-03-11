/******************************************************************************
 *
 * File:            PdfTools_PdfToolsImage2PdfProfiles.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSIMAGE2PDFPROFILES_H__
#define PDFTOOLS_PDFTOOLSIMAGE2PDFPROFILES_H__

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
#define PdfToolsImage2PdfProfiles_Archive_GetLanguage PdfToolsImage2PdfProfiles_Archive_GetLanguageW
#define PdfToolsImage2PdfProfiles_Archive_SetLanguage PdfToolsImage2PdfProfiles_Archive_SetLanguageW

#else
#define PdfToolsImage2PdfProfiles_Archive_GetLanguage PdfToolsImage2PdfProfiles_Archive_GetLanguageA
#define PdfToolsImage2PdfProfiles_Archive_SetLanguage PdfToolsImage2PdfProfiles_Archive_SetLanguageA

#endif

/******************************************************************************
 * Profile
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage2Pdf_ImageOptions* PDFTOOLS_CALL
PdfToolsImage2PdfProfiles_Profile_GetImageOptions(TPdfToolsImage2PdfProfiles_Profile* pProfile);

PDFTOOLS_EXPORT TPdfToolsImage2PdfProfiles_ProfileType PDFTOOLS_CALL
PdfToolsImage2PdfProfiles_Profile_GetType(TPdfToolsImage2PdfProfiles_Profile* pProfile);
/******************************************************************************
 * Default
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage2PdfProfiles_Default* PDFTOOLS_CALL PdfToolsImage2PdfProfiles_Default_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf_Conformance PDFTOOLS_CALL
PdfToolsImage2PdfProfiles_Default_GetConformance(TPdfToolsImage2PdfProfiles_Default* pDefault);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2PdfProfiles_Default_SetConformance(
    TPdfToolsImage2PdfProfiles_Default* pDefault, TPdfToolsPdf_Conformance iConformance);

/******************************************************************************
 * Archive
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsImage2PdfProfiles_Archive* PDFTOOLS_CALL PdfToolsImage2PdfProfiles_Archive_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf_Conformance PDFTOOLS_CALL
PdfToolsImage2PdfProfiles_Archive_GetConformance(TPdfToolsImage2PdfProfiles_Archive* pArchive);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2PdfProfiles_Archive_SetConformance(
    TPdfToolsImage2PdfProfiles_Archive* pArchive, TPdfToolsPdf_Conformance iConformance);
PDFTOOLS_EXPORT TPdfTools_StringList* PDFTOOLS_CALL
PdfToolsImage2PdfProfiles_Archive_GetAlternateText(TPdfToolsImage2PdfProfiles_Archive* pArchive);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsImage2PdfProfiles_Archive_SetAlternateText(
    TPdfToolsImage2PdfProfiles_Archive* pArchive, TPdfTools_StringList* pAlternateText);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsImage2PdfProfiles_Archive_GetLanguageA(
    TPdfToolsImage2PdfProfiles_Archive* pArchive, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsImage2PdfProfiles_Archive_GetLanguageW(
    TPdfToolsImage2PdfProfiles_Archive* pArchive, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsImage2PdfProfiles_Archive_SetLanguageA(TPdfToolsImage2PdfProfiles_Archive* pArchive, const char* szLanguage);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsImage2PdfProfiles_Archive_SetLanguageW(TPdfToolsImage2PdfProfiles_Archive* pArchive, const WCHAR* szLanguage);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSIMAGE2PDFPROFILES_H__ */
