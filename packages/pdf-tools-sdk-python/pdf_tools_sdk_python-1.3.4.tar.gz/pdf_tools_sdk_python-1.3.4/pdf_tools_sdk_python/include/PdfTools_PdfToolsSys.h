/******************************************************************************
 *
 * File:            PdfTools_PdfToolsSys.h
 *
 * Description:     Sytem declaration file
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 * Classification:  CONFIDENTIAL
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSSYS_H__
#define PDFTOOLS_PDFTOOLSSYS_H__

#include <stdarg.h>
#ifndef NO_FILE_STREAM_DESCRIPTOR
#include <stdio.h>
#endif

#ifdef __cplusplus
extern "C"
{
#endif

#ifdef _UNICODE
#define PdfToolsSys_PathStreamDescriptor_Create PdfToolsSys_PathStreamDescriptor_CreateW
#else
#define PdfToolsSys_PathStreamDescriptor_Create PdfToolsSys_PathStreamDescriptor_CreateA
#endif

typedef pos_t(STDCALL* TGetLength)(void* handle);
typedef int(STDCALL* TSeek)(void* handle, pos_t iPos);
typedef pos_t(STDCALL* TTell)(void* handle);
typedef size_t(STDCALL* TRead)(void* handle, void* pData, size_t nSize);
typedef size_t(STDCALL* TWrite)(void* handle, const void* pData, size_t nSize);
typedef void(STDCALL* TRelease)(void* handle);

typedef struct TPdfToolsSys_StreamDescriptor
{
    /** \brief Get length of stream in bytes */
    TGetLength pfGetLength;

    /** \brief Set position
     *  \param iPos byte position, -1 for end of stream
     *  \return 1 on success, 0 on failure
     */
    TSeek pfSeek;

    /** \brief Get current byte position
     *  \return byte position, -1 if position unknown
     */
    TTell pfTell;

    /** \brief Read nSize bytes from stream
     *  \return number of bytes read, 0 for end of stream, -1 for an error
     */
    TRead pfRead;

    /** \brief Write nSize bytes to stream
     *  \return number of bytes written, -1 for error (0 is interpreted as error too)
     */
    TWrite pfWrite;

    /** \brief Release handle */
    TRelease pfRelease;

    /** \brief Stream handle */
    void* m_handle;
} TPdfToolsSys_StreamDescriptor;

#ifndef NO_FILE_STREAM_DESCRIPTOR
/******************************************************************************
 * Stream descriptor for FILE*
 * (always use binary mode to fopen file!)
 *****************************************************************************/

static pos_t STDCALL PdfToolsSysFILEPtrGetLength__(void* handle)
{
    pos_t iPos, nLen;
    iPos = ftell((FILE*)handle);
    if (iPos == -1)
        return -1;
    if (fseek((FILE*)handle, 0L, SEEK_END) != 0)
        return -1;
    nLen = ftell((FILE*)handle);
    if (fseek((FILE*)handle, (long)iPos, SEEK_SET) != 0)
        return -1;
    return nLen;
}

static int STDCALL PdfToolsSysFILEPtrSeek__(void* handle, pos_t iPos)
{
    return fseek((FILE*)handle, (long)iPos, SEEK_SET) == 0 ? 1 : 0;
}

static pos_t STDCALL PdfToolsSysFILEPtrTell__(void* handle) { return ftell((FILE*)handle); }

static size_t STDCALL PdfToolsSysFILEPtrRead__(void* handle, void* pData, size_t nSize)
{
    size_t nRead = fread(pData, 1, nSize, (FILE*)handle);
    if (nRead != nSize && ferror((FILE*)handle) != 0)
        return (size_t)-1;
    return nRead;
}

static size_t STDCALL PdfToolsSysFILEPtrWrite__(void* handle, const void* pData, size_t nSize)
{
    if (fwrite(pData, 1, nSize, (FILE*)handle) != nSize)
        return (size_t)-1;
    return nSize;
}

static void STDCALL PdfToolsSysFILEPtrRelease__(void* handle) { fclose((FILE*)handle); }

static void PdfToolsSysCreateFILEStreamDescriptor(TPdfToolsSys_StreamDescriptor* pDescriptor, FILE* handle,
                                                  int bCloseOnRelease)
{
    pDescriptor->m_handle    = handle;
    pDescriptor->pfGetLength = &PdfToolsSysFILEPtrGetLength__;
    pDescriptor->pfSeek      = &PdfToolsSysFILEPtrSeek__;
    pDescriptor->pfTell      = &PdfToolsSysFILEPtrTell__;
    pDescriptor->pfRead      = &PdfToolsSysFILEPtrRead__;
    pDescriptor->pfWrite     = &PdfToolsSysFILEPtrWrite__;
    pDescriptor->pfRelease   = bCloseOnRelease ? &PdfToolsSysFILEPtrRelease__ : NULL; // NOLINT(modernize-use-nullptr)
}
#endif // NO_FILE_STREAM_DESCRIPTOR

/******************************************************************************
 * Path Stream Descriptor convenience function
 *****************************************************************************/

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSys_PathStreamDescriptor_CreateA(TPdfToolsSys_StreamDescriptor* pDescriptor,
                                                                            const char* szPath, BOOL bIsReadOnly);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSys_PathStreamDescriptor_CreateW(TPdfToolsSys_StreamDescriptor* pDescriptor,
                                                                            const WCHAR* szPath, BOOL bIsReadOnly);
PDFTOOLS_EXPORT void PDFTOOLS_CALL PdfToolsSys_PathStreamDescriptor_Close(TPdfToolsSys_StreamDescriptor* pDescriptor);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSSYS_H__ */
