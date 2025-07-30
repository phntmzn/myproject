#!/bin/bash
set -e

APP_NAME="myproject"
VERSION="0.1.0"
PKG_ID="com.myorg.myproject"
BUILD_DIR="build"
STAGE_DIR="$BUILD_DIR/pkgroot"
INSTALL_DIR="/usr/local/$APP_NAME"
FINAL_PKG="${APP_NAME}-${VERSION}.pkg"

echo "🧹 Cleaning previous build..."
rm -rf "$BUILD_DIR"
mkdir -p "$STAGE_DIR/usr/local/$APP_NAME"
mkdir -p "$STAGE_DIR/Library/LaunchAgents"

echo "🛠️ Building C++ library..."
cmake -S . -B "$BUILD_DIR"
cmake --build "$BUILD_DIR"

echo "📂 Staging files..."
cp "$BUILD_DIR/libmylib.dylib" "$STAGE_DIR/usr/local/$APP_NAME/"
cp -r python "$STAGE_DIR/usr/local/$APP_NAME/"
cp models/model.pt "$STAGE_DIR/usr/local/$APP_NAME/"
cp launchd/com.myorg.myproject.plist "$STAGE_DIR/Library/LaunchAgents/"
chmod +x scripts/postinstall.sh

echo "📦 Building component package..."
pkgbuild \
  --identifier "$PKG_ID" \
  --version "$VERSION" \
  --root "$STAGE_DIR" \
  --install-location "/" \
  --scripts scripts \
  "$BUILD_DIR/${APP_NAME}.pkg"

echo "📦 Building final product package..."
productbuild \
  --distribution pkg/Distribution.xml \
  --package-path "$BUILD_DIR" \
  "$FINAL_PKG"

echo "✅ Build complete: $FINAL_PKG"