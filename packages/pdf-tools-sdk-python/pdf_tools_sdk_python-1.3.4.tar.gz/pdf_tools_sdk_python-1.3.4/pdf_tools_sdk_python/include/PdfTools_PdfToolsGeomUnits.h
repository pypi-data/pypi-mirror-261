/******************************************************************************
 *
 * File:            PdfTools_PdfToolsGeomUnits.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSGEOMUNITS_H__
#define PDFTOOLS_PDFTOOLSGEOMUNITS_H__

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

PDFTOOLS_EXPORT double PDFTOOLS_CALL PdfToolsGeomUnits_Length_CreateFrom_inch(double dInches);
PDFTOOLS_EXPORT double PDFTOOLS_CALL PdfToolsGeomUnits_Length_CreateFrom_mm(double dMillimetres);
PDFTOOLS_EXPORT double PDFTOOLS_CALL PdfToolsGeomUnits_Length_ConvertTo_inch(double dLength);
PDFTOOLS_EXPORT double PDFTOOLS_CALL PdfToolsGeomUnits_Length_ConvertTo_mm(double dLength);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSGEOMUNITS_H__ */
