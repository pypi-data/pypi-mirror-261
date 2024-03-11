/******************************************************************************
 *
 * File:            PdfTools_PdfToolsOptimizationProfiles.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSOPTIMIZATIONPROFILES_H__
#define PDFTOOLS_PDFTOOLSOPTIMIZATIONPROFILES_H__

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
#else
#endif

/******************************************************************************
 * Profile
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsOptimization_ImageRecompressionOptions* PDFTOOLS_CALL
PdfToolsOptimizationProfiles_Profile_GetImageRecompressionOptions(TPdfToolsOptimizationProfiles_Profile* pProfile);
PDFTOOLS_EXPORT TPdfToolsOptimization_FontOptions* PDFTOOLS_CALL
PdfToolsOptimizationProfiles_Profile_GetFontOptions(TPdfToolsOptimizationProfiles_Profile* pProfile);
PDFTOOLS_EXPORT TPdfToolsOptimization_RemovalOptions* PDFTOOLS_CALL
PdfToolsOptimizationProfiles_Profile_GetRemovalOptions(TPdfToolsOptimizationProfiles_Profile* pProfile);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimizationProfiles_Profile_GetCopyMetadata(TPdfToolsOptimizationProfiles_Profile* pProfile);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimizationProfiles_Profile_SetCopyMetadata(
    TPdfToolsOptimizationProfiles_Profile* pProfile, BOOL bCopyMetadata);

PDFTOOLS_EXPORT TPdfToolsOptimizationProfiles_ProfileType PDFTOOLS_CALL
PdfToolsOptimizationProfiles_Profile_GetType(TPdfToolsOptimizationProfiles_Profile* pProfile);
/******************************************************************************
 * Web
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsOptimizationProfiles_Web* PDFTOOLS_CALL PdfToolsOptimizationProfiles_Web_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsOptimizationProfiles_Web_GetResolutionDPI(TPdfToolsOptimizationProfiles_Web* pWeb, double* pResolutionDPI);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimizationProfiles_Web_SetResolutionDPI(
    TPdfToolsOptimizationProfiles_Web* pWeb, const double* pResolutionDPI);

/******************************************************************************
 * Print
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsOptimizationProfiles_Print* PDFTOOLS_CALL PdfToolsOptimizationProfiles_Print_New(void);

/******************************************************************************
 * Archive
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsOptimizationProfiles_Archive* PDFTOOLS_CALL PdfToolsOptimizationProfiles_Archive_New(void);

/******************************************************************************
 * MinimalFileSize
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsOptimizationProfiles_MinimalFileSize* PDFTOOLS_CALL
PdfToolsOptimizationProfiles_MinimalFileSize_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimizationProfiles_MinimalFileSize_GetResolutionDPI(
    TPdfToolsOptimizationProfiles_MinimalFileSize* pMinimalFileSize, double* pResolutionDPI);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsOptimizationProfiles_MinimalFileSize_SetResolutionDPI(
    TPdfToolsOptimizationProfiles_MinimalFileSize* pMinimalFileSize, const double* pResolutionDPI);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSOPTIMIZATIONPROFILES_H__ */
