/******************************************************************************
 *
 * File:            PdfTools_PdfToolsPdf2ImageProfiles.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSPDF2IMAGEPROFILES_H__
#define PDFTOOLS_PDFTOOLSPDF2IMAGEPROFILES_H__

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
PDFTOOLS_EXPORT TPdfToolsPdf2Image_ContentOptions* PDFTOOLS_CALL
PdfToolsPdf2ImageProfiles_Profile_GetContentOptions(TPdfToolsPdf2ImageProfiles_Profile* pProfile);

PDFTOOLS_EXPORT TPdfToolsPdf2ImageProfiles_ProfileType PDFTOOLS_CALL
PdfToolsPdf2ImageProfiles_Profile_GetType(TPdfToolsPdf2ImageProfiles_Profile* pProfile);
/******************************************************************************
 * Fax
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2ImageProfiles_Fax* PDFTOOLS_CALL PdfToolsPdf2ImageProfiles_Fax_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf2Image_FaxImageOptions* PDFTOOLS_CALL
PdfToolsPdf2ImageProfiles_Fax_GetImageOptions(TPdfToolsPdf2ImageProfiles_Fax* pFax);
PDFTOOLS_EXPORT TPdfToolsPdf2Image_RenderPageAsFax* PDFTOOLS_CALL
PdfToolsPdf2ImageProfiles_Fax_GetImageSectionMapping(TPdfToolsPdf2ImageProfiles_Fax* pFax);

/******************************************************************************
 * Archive
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2ImageProfiles_Archive* PDFTOOLS_CALL PdfToolsPdf2ImageProfiles_Archive_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf2Image_ImageOptions* PDFTOOLS_CALL
PdfToolsPdf2ImageProfiles_Archive_GetImageOptions(TPdfToolsPdf2ImageProfiles_Archive* pArchive);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2ImageProfiles_Archive_SetImageOptions(
    TPdfToolsPdf2ImageProfiles_Archive* pArchive, TPdfToolsPdf2Image_ImageOptions* pImageOptions);
PDFTOOLS_EXPORT TPdfToolsPdf2Image_RenderPageAtResolution* PDFTOOLS_CALL
PdfToolsPdf2ImageProfiles_Archive_GetImageSectionMapping(TPdfToolsPdf2ImageProfiles_Archive* pArchive);

/******************************************************************************
 * Viewing
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf2ImageProfiles_Viewing* PDFTOOLS_CALL PdfToolsPdf2ImageProfiles_Viewing_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf2Image_ImageOptions* PDFTOOLS_CALL
PdfToolsPdf2ImageProfiles_Viewing_GetImageOptions(TPdfToolsPdf2ImageProfiles_Viewing* pViewing);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2ImageProfiles_Viewing_SetImageOptions(
    TPdfToolsPdf2ImageProfiles_Viewing* pViewing, TPdfToolsPdf2Image_ImageOptions* pImageOptions);
PDFTOOLS_EXPORT TPdfToolsPdf2Image_ImageSectionMapping* PDFTOOLS_CALL
PdfToolsPdf2ImageProfiles_Viewing_GetImageSectionMapping(TPdfToolsPdf2ImageProfiles_Viewing* pViewing);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf2ImageProfiles_Viewing_SetImageSectionMapping(
    TPdfToolsPdf2ImageProfiles_Viewing* pViewing, TPdfToolsPdf2Image_ImageSectionMapping* pImageSectionMapping);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSPDF2IMAGEPROFILES_H__ */
