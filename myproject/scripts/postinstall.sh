#!/bin/bash

echo "🔧 Post-install script running..."

# Load LaunchAgent if plist is installed
PLIST_PATH="/Library/LaunchAgents/com.myorg.myproject.plist"
if [ -f "$PLIST_PATH" ]; then
    echo "📦 Loading LaunchAgent: $PLIST_PATH"
    launchctl load "$PLIST_PATH"
else
    echo "⚠️ LaunchAgent not found at $PLIST_PATH"
fi

# Set permissions if needed
chmod +x /usr/local/bin/myproject-entrypoint || echo "ℹ️ Entrypoint script not found or already executable."

echo "✅ Post-install script completed."
