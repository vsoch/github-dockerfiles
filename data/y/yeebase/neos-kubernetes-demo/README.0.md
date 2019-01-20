=============================================================================
Flow Configuration Directory
=============================================================================

This directory contains the configuration for the Flow framework and the
application based on it. The configuration files only contain additions and
modifications of the original configuration and therefore don't contain all
possible configuration options.

The following files play a role in the configuration system:

   Settings.yaml    Various application-level settings can be set in this file.

   Objects.yaml     Additional objects configuration, overriding the
                    configuration which was defined in the various packages.

   Routes.yaml      Provides the routing configuration for the MVC framework.

   Views.yaml       Can be used to influence resolutions of views in MVC.

   Policy.yaml      Provides the configuration for the security framework.

   Caches.yaml      Provides the configuration for the caching framework.

All of these files become active in any application context if they reside
in the main Configuration directory (the same directory where this README is
located). However, context-specific configuration may be defined in sub directories
which carry the same name as the application context. These configuration
files are loaded after the default and global configuration has been invoked.