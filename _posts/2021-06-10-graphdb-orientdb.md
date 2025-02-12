---
layout: post
title: Setup und Use Orientdb 
categories: [Orientdb]
tags: [db, ui, graph, graph, java]
--- 
![](../pics/20230707122115_orientdb.png)

OrientDB - the first Multi-Model Open Source NoSQL DBMS that brings together the power of graphs and the flexibility of documents into one scalable high-performance operational database
- [Install OrientDB](#install-orientdb)
  - [Prepare](#prepare)
  - [Windows Service](#windows-service)
  - [Links](#links)

# Install OrientDB

* Versions 3.1.4, Lizenz: Apache V2.0 
* V 3.2.x *
* Graph DB für technische Datenfluss Dokumentation

## Prepare

* Openjdk-8-jdk or Oracle Java 8 server Win
* Apache commons-daemon 

## Windows Service

File: installserviceBat

```bat
:: OrientDB Windows Service Installation

rem installservice.bat c:\tmp\server-jre-8u291-windows-x64\jdk1.8.0_291\jre\bin\server\jvm.dll c:\tmp\orientdb-3.2.0
@echo off
rem Remove surrounding quotes from the first parameter
set str=%~1
rem Check JVM DLL location parameter
if "%str%" == "" goto missingJVM
set JVM_DLL=%str%
rem Remove surrounding quotes from the second parameter
set str=%~2
rem Check OrientDB Home location parameter
if "%str%" == "" goto missingOrientDBHome
set ORIENTDB_HOME=%str%

set CONFIG_FILE=%ORIENTDB_HOME%/config/orientdb-server-config.xml
set LOG_FILE=%ORIENTDB_HOME%/config/orientdb-server-log.properties
set LOG_CONSOLE_LEVEL=info
set LOG_FILE_LEVEL=fine
set WWW_PATH=%ORIENTDB_HOME%/www
set ORIENTDB_ENCODING=UTF8
set ORIENTDB_SETTINGS=-Dprofiler.enabled=true -Dcache.level1.enabled=false -Dcache.level2.strategy=1
set JAVA_OPTS_SCRIPT=-XX:+HeapDumpOnOutOfMemoryError

rem Install service
OrientDBGraph.exe //IS --DisplayName="OrientDB" ^
--Description="OrientDB V3.2.0" ^
--StartClass=com.orientechnologies.orient.server.OServerMain --StopClass=com.orientechnologies.orient.server.OServerShutdownMain --StopParams=-p ++StopParams=p ^
--Classpath="%ORIENTDB_HOME%\lib\*" --JvmOptions=-Dfile.encoding=%ORIENTDB_ENCODING%;-Djava.util.logging.config.file="%LOG_FILE%";-Dorientdb.config.file="%CONFIG_FILE%";-Dorientdb.www.path="%WWW_PATH%";-Dlog.console.level=%LOG_CONSOLE_LEVEL%;-Dlog.file.level=%LOG_FILE_LEVEL%;-Dorientdb.build.number="@BUILD@";-DORIENTDB_HOME="%ORIENTDB_HOME%" ^
--StartMode=jvm --StartPath="%ORIENTDB_HOME%\bin" --StopMode=jvm --StopPath="%ORIENTDB_HOME%\bin" --Jvm="%JVM_DLL%" --LogPath="%ORIENTDB_HOME%\log" --Startup=auto

EXIT /B

:missingJVM
echo Insert the JVM DLL location
goto printUsage

:missingOrientDBHome
echo Insert the OrientDB Home
goto printUsage

:printUsage
echo usage:
echo     installService JVM_DLL_location OrientDB_Home
EXIT /B
```

File: uninstallservice.bat

```bat

:: OrientDB Windows Service Uninstallation
@echo off
rem Uninstall service
OrientDBGraph.exe //DS
```

## Links

<https://github.com/orientechnologies/orientdb/issues/6552>

<https://github.com/orientechnologies/orientdb/issues/2785>

<https://downloads.apache.org/commons/daemon/binaries/windows/>

<http://commons.apache.org/proper/commons-daemon/download_daemon.cgi>

<https://orientdb.org/docs/3.1.x/admin/Windows-Service.html>

<https://github.com/orientechnologies/orientdb-docker>

<http://orientdb.com/docs/3.1.x/admin/installation/>

<https://orientdb.org/download-previous>

<https://orientdb.org/download>
