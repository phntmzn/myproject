#!/bin/bash
set -e

APP_DIR="/usr/local/myproject"
PLIST="/Library/LaunchAgents/com.myorg.myproject.plist"

echo "🧼 Uninstalling myproject..."

# Unload LaunchAgent
if [ -f "$PLIST" ]; then
    echo "↪️  Unloading LaunchAgent..."
    launchctl unload "$PLIST" || true
    rm -f "$PLIST"
fi

# Remove app files
if [ -d "$APP_DIR" ]; then
    echo "🗑️  Removing $APP_DIR"
    rm -rf "$APP_DIR"
fi

echo "✅ Uninstall complete."