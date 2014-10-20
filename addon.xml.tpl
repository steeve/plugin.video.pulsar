<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="plugin.video.pulsar" name="Pulsar" version="$VERSION" provider-name="steeve">
    <requires>
        <import addon="xbmc.python" version="2.1.0"/>
    </requires>
    <extension point="xbmc.addon.repository" name="Pulsar Repository">
        <info compressed="false">http://localhost:10001/repository/steeve/plugin.video.pulsar/addons.xml</info>
        <checksum>http://localhost:10001/repository/steeve/plugin.video.pulsar/addons.xml.md5</checksum>
        <datadir zip="true">http://localhost:10001/repository/steeve/</datadir>
    </extension>
    <extension point="xbmc.python.pluginsource" library="main.py">
        <provides>video</provides>
    </extension>
    <extension point="xbmc.service" library="pulsard.py" start="login"/>
    <extension point="xbmc.python.module" library="resources/site-packages" />
    <extension point="xbmc.addon.metadata">
        <platform>all</platform>
        <language></language>
    </extension>
</addon>
