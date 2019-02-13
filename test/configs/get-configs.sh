#!/bin/bash
for i in cl_support_en*; do TARGET=`echo $i | sed s/cl_support_en//g | sed s/sw//g | cut -d_ -f1`; echo $TARGET; mkdir -p configs/$TARGET ; mkdir -p configs/$TARGET/etc/network/; cp -pr $i/etc/network/interfaces configs/$TARGET/etc/network/; mkdir -p configs/$TARGET/etc/frr; cp -pr $i/etc/frr/* configs/$TARGET/etc/frr; done

